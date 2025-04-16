def edit_server_properties(
    file_path='server.properties',
    world_name='ChopinWorld',
    level_seed='123456',
    gamemode='creative',
    difficulty='easy',
    allow_cheats=True
):
    settings = {
        'level-name': world_name,
        'level-seed': level_seed,
        'gamemode': gamemode,
        'difficulty': difficulty,
        'allow-cheats': str(allow_cheats).lower(),
    }

    # Read the current file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update or insert settings
    updated_lines = []
    for line in lines:
        key = line.split('=')[0].strip()
        if key in settings:
            updated_lines.append(f"{key}={settings[key]}\n")
            del settings[key]  # remove from dict after writing
        else:
            updated_lines.append(line)

    # Append any new keys not found before
    for key, value in settings.items():
        updated_lines.append(f"{key}={value}\n")

    # Write back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

    print(f"Updated {file_path} successfully.")

# Example usage:
edit_server_properties(
    file_path='server.properties',
    world_name='Terraria',
    level_seed='987654',
    gamemode='survival',
    difficulty='normal',
    allow_cheats=True
)
