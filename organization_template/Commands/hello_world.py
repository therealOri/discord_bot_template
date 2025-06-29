import asyncio



async def hello_main(interaction):
    await interaction.response.send_message("Hello world!", ephemeral=True, delete_after=10)






















if __name__ == '__main__':
    pass
