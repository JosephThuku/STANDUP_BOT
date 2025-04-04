import os
import discord
import asyncio
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True  # Needed for on_member_join

bot = commands.Bot(command_prefix="!", intents=intents)
scheduler = AsyncIOScheduler()

user_responses = {}
user_points = {}

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    scheduler.add_job(standup_reminder, "cron", hour=10, minute=0)
    scheduler.add_job(reminder_for_non_responders, "cron", hour=12, minute=0)
    scheduler.start()

@bot.event
async def on_member_join(member):
    if not member.bot:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(
                f"👋 Welcome {member.mention}!\n"
                "**Here's how to submit your daily standup:**\n"
                "Every day at **10 AM**, the bot will ask:\n"
                "1️⃣ What did you work on yesterday?\n"
                "2️⃣ What will you work on today?\n"
                "3️⃣ Any blockers?\n"
                "Just reply in the channel within 2 hours to earn points! 🏆"
            )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == CHANNEL_ID:
        if message.author.id not in user_responses:
            user_responses[message.author.id] = True
            user_points[message.author.id] = user_points.get(message.author.id, 0) + 1
            await message.channel.send(f"✅ {message.author.mention}, thanks for your standup! You've earned 1 point. Total: {user_points[message.author.id]} 🏅")

    if bot.user in message.mentions:
        await message.channel.send("👋 Hey there! I'm your daily standup bot. Use `!quiz` to learn how I work!")

    await bot.process_commands(message)

@bot.command(name="quiz")
async def quiz(ctx):
    await ctx.send("📘 Let's see how much you know! Answer with `1`, `2`, or `3`.")
    await ctx.send(
        "**What time does the standup reminder get sent?**\n"
        "1. 8 AM\n"
        "2. 10 AM\n"
        "3. 12 PM"
    )

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content in ["1", "2", "3"]

    try:
        msg = await bot.wait_for("message", check=check, timeout=15.0)
        if msg.content == "2":
            await ctx.send("✅ Correct! You're ready for standups! 🎉")
        else:
            await ctx.send("❌ Oops, the correct answer is 2 (10 AM). Try again later!")
    except asyncio.TimeoutError:
        await ctx.send("⌛ Time's up! Try the `!quiz` command again when you're ready.")

async def standup_reminder():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(
            "**⏰ Daily Standup Time!**\n"
            "1️⃣ What did you work on yesterday?\n"
            "2️⃣ What will you work on today?\n"
            "3️⃣ Any blockers?\n\n"
            "👉 Please reply in the next 2 hours to earn points!"
        )
        user_responses.clear()

async def reminder_for_non_responders():
    channel = bot.get_channel(CHANNEL_ID)
    guild = bot.get_guild(GUILD_ID)

    if channel and guild:
        members = [m for m in guild.members if not m.bot]
        non_responders = [m.mention for m in members if m.id not in user_responses]

        if non_responders:
            await channel.send(
                f"⏳ **Reminder:** {', '.join(non_responders)}, don't forget to submit your standup!"
            )

@bot.command(name="points")
async def check_points(ctx):
    points = user_points.get(ctx.author.id, 0)
    await ctx.send(f"🏆 {ctx.author.mention}, you have {points} standup points!")

bot.run(TOKEN)
