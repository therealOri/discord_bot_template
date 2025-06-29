import asyncio



async def add(interaction, num1, num2):
    lst = [num1, num2]
    for _ in lst:
        if isinstance(_, int):
            pass
        else:
            return 000, "Number passed is not type 'int'."

    result = num1 + num2
    await interaction.response.send_message(f"Your results is: {str(result)}", ephemeral=True, delete_after=10)






















if __name__ == '__main__':
    pass
