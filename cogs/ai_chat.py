from discord.ext import commands
from discord import app_commands
import discord

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class AIChat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ai",
        description="Talk with Xyth AI"
    )
    async def ai(
        self,
        interaction: discord.Interaction,
        question: str
    ):

        await interaction.response.defer()

        try:

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Xyth, a futuristic AI Discord assistant. "
                            "You are smart, friendly, and helpful."
                        )
                    },

                    {
                        "role": "user",
                        "content": question
                    }
                ],

                temperature=0.7,
                max_tokens=300
            )

            ai_response = response.choices[0].message.content

            embed = discord.Embed(
                title="🤖 Xyth AI",
                description=ai_response,
                color=discord.Color.purple()
            )

            embed.set_footer(
                text=f"Requested by {interaction.user}"
            )

            await interaction.followup.send(
                embed=embed
            )

        except Exception as e:

            await interaction.followup.send(
                f"Error: {e}"
            )

async def setup(bot):
    await bot.add_cog(AIChat(bot))