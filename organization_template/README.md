# About
This template is for if you want to keep things more organized but aren't using cogs. I figured that a discord command is just a regular async function, and you can call other functions from within functions.

So I thought, why not just import the functions I need into the main code and then call said code in the command/event functions instead of creating 1 big massive main file with thousands of lines of code.
And that's what this template is about, importing and using functions instead of making a massive singular file. AND without having to use cogs.
__ __

<br>
<br>

# Example
```python
@tmp.tree.command(description='says hello world!')
async def hello_world(interaction: discord.Interaction):
    from Commands import hello_world as cmd
    await cmd.hello_main(interaction)
```
> This is the main command function that will import and use the following code imported from the `Commands` folder.

<br>

```python
async def hello_main(interaction):
    await interaction.response.send_message("Hello world!", ephemeral=True, delete_after=10)
```
> The result is an ephemeral message getting sent to the channel the command was used in saying "Hello world!" and dissapearing after 10s.
__ __
