# All "global" environment variables (such as filename, path to db file) are stored here for
# easy access and modification


class ENV:
    # Name of the database file (with extension)
    db_name = 'qskm.db'

    # TODO: check if this is ok in production environment
    # Relative path of the database file in the project
    rel_db_path = 'db\\{}'.format(db_name)

    # Name of the table that stores all data related to the game, including
    # id (transparent to user), name of the game, key/url of the game, notes, category, and more
    game_table_name = 'Games'

    # Default db file chooser path (used in conjunction with expanduser() func)
    default_db_folder_path = '~/Documents/'

    # GitHub project page
    github_project_page = 'https://github.com/l19980623/QSteamKeyManager'

    # WEB URL TEMPLATES
    # Here you can find predefined web URLs to many popular storefronts.
    # Used to search and activate games on these stores
    # -- Search URLs
    # ---- Steam
    steam_search_url = 'https://store.steampowered.com/search/?term={}'

    # ---- GOG
    # ---- NOTE: GOG doesn't have a dedicated page for searching, only APIs. Showing main page for now
    gog_search_url = 'https://www.gog.com/'

    # ---- itch.io
    itch_search_url = 'https://itch.io/search?q={}'

    # ---- Origin
    # ---- NOTE: Original format is https://www.origin.com/[country]/[lang]/search?searchString=[search term]
    # ----       however I found that if I remove the country and lang from the URL it will select country based on
    # ----       user's cookies, then use IP address to determine story country, which is better than hard-coded
    #            country string
    origin_search_url = 'https://www.origin.com/search?searchString={}'

    # ---- Ubi Store (Uplay)
    # ---- NOTE: Original format is https://store.ubi.com/[country]/search/?q=[search term]&lang=[lang]
    # ----       by removing some extraneous attributes it will follow the user's country preference on cookies
    # ----       then use IP address to determine the store country, which is better than hard-coding country in URL
    uplay_search_url = 'https://store.ubi.com/search/?q={}'

