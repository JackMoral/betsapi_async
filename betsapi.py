
class BetsAPI:

    r_sport_id = {
        '1': 'Soccer',
        '2': 'Horse Racing',
        '3': 'Cricket',
        '4': 'Greyhounds',
        '8': 'Rugby Union',
        '9': 'Boxing/UFC',
        '12': 'American Football',
        '13': 'Tennis',
        '14': 'Snooker',
        '15': 'Darts',
        '16': 'Baseball',
        '17': 'Ice Hockey',
        '18': 'Basketball',
        '19': 'Rugby League',
        '36': 'Australian Rules',
        '66': 'Bowls',
        '75': 'Gaelic Sports',
        '78': 'Handball',
        '83': 'Futsal',
        '90': 'Floorball',
        '91': 'Volleyball',
        '92': 'Table Tennis',
        '94': 'Badminton',
        '95': 'Beach Volleyball',
        '107': 'Squash',
        '110': 'Water Polo',
        '151': 'E-sports',
    }

    r_errors = {
        'INTERNAL_SERVER_ERROR': '500 Internal Server Error, contact Support if it happens',
        'NOT_FOUND': '404 Not Found',
        'METHOD_NOT_ALLOWED': 'Method is not allowed, only GET is supported.',
        'UNDER_MAINTENANCE': "API is under maintenance, we'll annouce it",
        'AUTHORIZE_FAILED': 'Token is not provided or incorrect.',
        'TOO_MANY_REQUESTS': 'API rate limit exceeded.',
        'PERMISSION_DENIED': "You're not allowed, contact Support if it is wrong.",
        'PARAM_REQUIRED': 'Required param is missing, check error_detail for details',
        'PARAM_INVALID': 'param is invalid, check error_detail for details'
    }

    r_pager = {
        'page': 'Current page',
        'per_page': 'how many results per page, default to 50 as always',
        'total': 'how many results in total. use it to indicate that it has next page or not'
    }

    time_status = {
        '0': 'Not Started',
        '1': 'InPlay',
        '2': 'TO BE FIXED',
        '3': 'Ended',
        '4': 'Postponed',
        '5': 'Cancelled',
        '6': 'Walkover',
        '7': 'Interrupted',
        '8': 'Abandoned',
        '9': 'Retired',
        '99': 'Removed',
    }

    player_type_ids = {
        '1': 'Player',
        '3': 'Manager',
        '8': 'On loan',
    }

    tennis_ranking_type_ids = {
        '1': 'Singles Men',
        '2': 'Doubles Men',
        '3': 'Singles Women',
        '4': 'Doubles Women',
    }

    round_ids = {
        '1': 'Final',
        '2': 'Semifinals',
        '3': 'Quarterfinals',
        '4': '1/8',
        '5': '1/16',
        '6': '1/32',
        '7': 'Round 1',
        '8': 'Round 2',
        '9': 'Round 3',
        '10': 'Round 4',
        '11': 'Round 5',
        '12': 'Round 6',
        '14': 'Qualification round 1',
        '15': 'Qualification round 2',
        '16': 'Qualification round 3',
        '17': 'Qualification round 4',
        '20': 'Bronze',
        '23': 'R128',
        '24': 'R64',
        '25': 'R32',
        '26': 'R16',
        '27': 'Quarterfinals',
        '28': 'Semifinals',
        '29': 'Final',
        '31': '5th place final',
        '32': '7th place final',
        '33': '9th place final',
        '34': '13th place final',
        '35': '11th place final',
        '36': 'Round 7',
        '39': '15th place final',
        '40': '17th place final',
        '41': '19th place final',
        '42': '21st place final',
        '43': '23rd place final',
        '44': 'Qualification round',
        '45': 'Qualification round',
        '46': 'Qualification round',
        '48': 'Placement qualification match',
        '49': 'Placement match for 2nd',
        '50': 'Placement match for 3rd',
        '54': 'Qualification round',
        '57': 'R128',
        '60': 'Qualification round',
        '62': 'Qualification round',
        '63': "Winners' Finals",
        '64': 'Qualification round',
        '65': "Losers' Finals",
        '67': "Winners' Semifinals",
        '69': "Losers' Semifinals",
        '71': "Winners' Quarterfinals",
        '73': "Losers' Quarterfinals",
        '79': "Winners' Round 1",
        '81': "Losers' Round 1",
        '83': "Winners' Round 2",
        '85': "Losers' Round 2",
        '89': "Losers' Round 3",
        '93': "Losers' Round 4",
        '97': "Losers' Round 5",
        '99': "Winners' Match",
        '101': "Losers' Match",
        '103': 'Decider match',
        '105': 'Initial match',
        '106': 'Round 1 Semifinal',
        '110': 'Wild Card',
        '122': 'First Round',
        '124': 'Second Round',
        '126': 'Conference Finals',
        '128': 'Stanley Cup Final',
        '132': 'Conference Semifinals',
        '134': 'NBA Finals',
        '140': 'Final Four',
        '142': 'Championship',
        '146': 'World Series',
        '148': 'Preliminary Round',
        '150': 'Extra Preliminary Round',
        '164': 'Qualification round',
        '166': 'Qualification round',
        '173': 'AL Wild Card',
        '177': 'ALCS',
        '179': 'ALDS',
        '183': 'Eastern Conference Finals',
        '189': 'Eastern Conference First Round',
        '195': 'Eastern Conference Semifinals',
        '197': 'Eastern Conference Second Round',
        '199': 'MLS Cup',
        '207': 'NL Wild Card',
        '211': 'NLCS',
        '213': 'NLDS',
        '217': 'Western Conference Finals',
        '221': 'Western Conference First Round',
        '227': 'Western Conference Semifinals',
        '231': 'Western Conference Second Round',
        '232': 'Preliminary Finals',
        '271': 'Round Robin',
        '273': 'Division Semifinals',
        '275': 'Division Finals',
        '392': 'Round 2 Final',
        '394': 'Grand Final',
        '398': 'First Four',
        '400': 'National Championship',
        '402': 'East Regional - Elite Eight',
        '404': 'East Regional - First Round',
        '406': 'East Regional - Second Round',
        '408': 'East Regional - Sweet 16',
        '412': 'Midwest Regional - Elite Eight',
        '414': 'Midwest Regional - First Round',
        '416': 'Midwest Regional - Second Round',
        '418': 'Midwest Regional - Sweet 16',
        '422': 'South Regional - Elite Eight',
        '424': 'South Regional - First Round',
        '426': 'South Regional - Second Round',
        '428': 'South Regional - Sweet 16',
        '432': 'West Regional - Elite Eight',
        '434': 'West Regional - First Round',
        '436': 'West Regional - Second Round',
        '438': 'West Regional - Sweet 16'
    }

    language_ids = {
        '1': 'English (by default)',
        '2': 'zh_TW (繁體中文)',
        '3': 'es_ES (Español)',
        '5': 'de_DE (Deutsch)',
        '6': 'it_IT (Italiano)',
        '7': 'da_DK (Dansk)',
        '8': 'sv_SE (Svenska)',
        '9': 'nn_NO (Norsk)',
        '10': 'zh_CN (简体中文)',
        '19': 'bg_BG (Български)',
        '20': 'el_GR (Ελληνικά)',
        '21': 'pl_PL (Polski)',
        '22': 'pt_PT (Português)',
        '23': 'ro_RO (Română)',
        '24': 'cs_CZ (Česky)',
        '25': 'hu_HU (Magyar)',
        '26': 'sk_SK (Slovenčina)',
        '28': 'nl_NL (Nederlands)',
        '29': 'et_EE (Eesti)',
        '31': 'ru_RU (Русский)',
        '34': 'ja_JP (日本語)',
        '71': 'ko_KR (한국어)',
        '72': 'fr_FR (Français)'
    }

    bet365_fields_explanation = {
        '3P': 'PLACE_365',
        '3W': 'WIN_365',
        '4Q': 'MARKET_GROUP_PAIR_ID',
        'AB': 'FINANCIALS_PRICE_1',
        'AC': 'STATS_COLUMN',
        'AD': 'ADDITIONAL_DATA, TEAM_TOUCHDOWN_QUOTE',
        'AE': 'STATS_CELL',
        'AF': 'ARCHIVE_FIXTURE_INFO',
        'AH': 'ASIAN_HOVER, FINANCIALS_MARKET_ODDS_1',
        'AI': 'ANIMATION_ID',
        'AJ': 'FINANCIALS_MARKET_ODDS_2',
        'AM': 'ANIMATION_ICON',
        'AO': 'ANIMATION_TOPIC',
        'AP': 'STATS_PANE',
        'AQ': 'FINANCIALS_CLOSE_TIME',
        'AS': 'ADDITIONAL_STATS, ANIMATION_SOUND, TEAM_FIELDGOAL_QUOTE',
        'AT': 'ANIMATION_TEXT, STATS_TAB',
        'AU': 'AUDIO_AVAILABLE',
        'AV': 'ARCHIVE_VIDEO_AVAILABLE',
        'BB': 'BUTTON_BAR',
        'BC': 'BOOK_CLOSES, CLOSE_BETS_COUNT',
        'BD': 'PULL_BET_DATA',
        'BE': 'BET',
        'BH': 'BLURB_HEADER',
        'BI': 'BUTTON_BAR_INDEX, BUTTON_SPLIT_INDEX',
        'BL': 'BASE_LINE',
        'BO': 'BASE_ODDS, OPEN_BETS_COUNT',
        'BS': 'BANNER_STYLE',
        'BT': 'INFO_POD_DETAIL_2',
        'C1': 'C1_ID, MINI_DIARY_C1',
        'C2': 'C2_ID, MINI_DIARY_C2',
        'C3': 'MINI_DIARY_C3',
        'CB': 'CLOSE_BETS_DISABLED, EXCLUDED_COUNTRIES, FINANCIALS_MARKET_NAME, CLOSE_BETS_ENABLED',
        'CC': 'BET_TYPE_PULL, COMPETITION_CODE',
        'CD': 'COMPETITION_DROPDOWN, FINANCIALS_TRADE',
        'CF': 'CONFIG',
        'CG': 'GLOBAL_CONFIG',
        'CI': 'CLASS_ID, MINI_DIARY, CUP_ICON',
        'CK': 'COMPETITION_KEY',
        'CL': 'CLASSIFICATION',
        'CM': 'BET_CALL_FEATURE_DISABLED, COMMENT',
        'CN': 'CHANNEL, COLUMN_NUMBER',
        'CO': 'COLUMN',
        'CP': 'CLOSE_BETS_PRESENTATION_PULL_DISABLED, CURRENT_PROGRESS, CURRENT_PERIOD',
        'CR': 'CLASS_ORDER, CLOSE_BET_RETURNS',
        'CS': 'CLASSIFICATIONS',
        'CT': 'COMPETITION_NAME',
        'CU': 'CURRENT_INFO',
        'D1': 'DATA_1',
        'D2': 'DATA_2',
        'D3': 'DATA_3',
        'D4': 'DATA_4',
        'D5': 'DATA_5',
        'DA': 'DIARY_DAY',
        'DC': 'DISPLAY_CLOCK',
        'DD': 'DISPLAY_DATE',
        'DE': 'DESCRIPTION',
        'DM': 'IN_PLAY_LAUNCHER_DISPLAY_MODE',
        'DN': 'DIARY_NAME, DRAW_NUMBER',
        'DO': 'DEFAULT_OPEN',
        'DP': 'DECIMAL_PLACES',
        'DR': 'DIARY_REFRESH',
        'DS': 'DISPLAY_SCORE',
        'DX': 'DISABLE_COLUMN_DISTRIBUTION',
        'DY': 'DIARY',
        'EA': 'EVENT_TIME',
        'EC': 'ERROR_CODE, EXCLUDED_COUNTRY_CODES',
        'ED': 'EXTRA_DATA_2, TEAM_ODDS_A',
        'EE': 'ETOTE_LINK_DATA',
        'EI': 'EVENT_ID',
        'EL': 'EXTRA_STATS_AVAILABLE',
        'EM': 'EMPTY',
        'EP': 'EXTRA_PARTICIPANTS',
        'ER': 'ERROR_LOGGING',
        'ES': 'EMBEDDED_STREAMING, EXTRA_SCORES',
        'ET': 'END_TIME, EVENT_TYPE',
        'EV': 'EVENT',
        'EW': 'EACH_WAY',
        'EX': 'EXTRA_DATA_1, TEAM_ODDS_H',
        'FD': 'FORCE_DISPLAY',
        'FF': 'FILTERING',
        'FI': 'FIXTURE_PARENT_ID',
        'FK': 'FINANCIALS_FEED_1',
        'FL': 'FINANCIALS_PERIOD_1, APN_FLUC',
        'FM': 'FINANCIALS_MARKET_1A',
        'FN': 'FINANCIALS_MARKET_1B',
        'FO': 'FINANCIALS_FEED_2, FORM_PULL',
        'FP': 'FINANCIALS_PERIOD_2, FIXED_PLACE',
        'FQ': 'FINANCIALS_MARKET_2A',
        'FR': 'FINANCIALS_MARKET_2B',
        'FS': 'FIXTURE_STARTED',
        'FW': 'FIXED_WIN',
        'GC': 'LOTTO_GAME_CODE',
        'GM': 'LOTTO_GAME_MARKET',
        'GR': 'GROUP',
        'HA': 'HANDICAP',
        'HD': 'HANDICAP_FORMATTED',
        'HI': 'HEADER_IMAGE, BET_HISTORY',
        'HM': 'MARKET_BAR',
        'HO': 'DEFAULT_OPEN_HOMEPAGE',
        'HP': 'SHOW_ON_HOMEPAGE',
        'HS': 'HASH',
        'HT': 'POD_HEADER_TEXT',
        'HU': 'INFO_BANNER_SUBHEAD2',
        'HV': 'POD_BODY_TEXT_2',
        'HW': 'HORSE_WEIGHT',
        'HY': 'HORSE_AGE',
        'I2': 'ID2',
        'IA': 'AUDIO_ICON, DIARY_AUDIO_AVAILABLE',
        'IB': 'IBOX',
        'IC': 'ICON',
        'ID': 'ID',
        'IF': 'IN_PLAY',
        'IG': 'IMAGE_ID',
        'IM': 'IMAGE, INCLUDE_OVERVIEW_MARKET',
        'IN': 'INFO, INFO_POD_IMAGE_URL',
        'IO': 'ITEM_ORDER',
        'IP': 'IN_PLAY_AVAILABLE_FLAG, PARENT_ID',
        'IQ': 'INFO_POD_IMAGE1',
        'IR': 'INRUNNING_INFO',
        'IS': 'INFO_POD_IMAGE_PATH1',
        'IT': 'TOPIC_ID',
        'IU': 'INFO_POD_IMAGE2',
        'JN': 'JOCKEY_PULL',
        'JY': 'JOCKEY',
        'KC': 'KIT_COLORS',
        'KI': 'KIT_ID',
        'L1': 'BREADCRUMB_LEVEL_1',
        'LA': 'LABEL, INFO_POD_LINK_1_ID',
        'LB': 'INFO_POD_LINK_1_DISPLAY_TEXT',
        'LC': 'EVENT_COUNT, INFO_POD_LINK_1_C1_ID',
        'LD': 'INFO_POD_LINK_1_C1_ID_TABLE',
        'LE': 'INFO_POD_LINK_1_C2_ID',
        'LF': 'INFO_POD_LINK_1_C2_ID_TABLE',
        'LG': 'INFO_POD_LINK_2_ID, SOCCER_LEAGUE',
        'LH': 'INFO_POD_LINK_2_DISPLAY_TEXT',
        'LI': 'INFO_POD_LINK_2_C1_ID',
        'LJ': 'INFO_POD_LINK_2_C1_ID_TABLE',
        'LK': 'INFO_POD_LINK_2_C2_ID',
        'LL': 'INFO_POD_LINK_2_C2_ID_TABLE',
        'LM': 'POD_ENCODED_URL_1, LIVE_MARKETS',
        'LN': 'POD_ENCODED_URL_2',
        'LO': 'DEFAULT_OPEN_LEFT',
        'LP': 'LIVE_IN_PLAY, INFO_POD_LINK_1_C3_ID',
        'LQ': 'INFO_POD_LINK_1_C3_ID_TABLE',
        'LR': 'INFO_POD_LINK_1_C3_SECTION_ID, LAST_RACES',
        'LS': 'PREVIOUS_SET_SCORE, SELECTED',
        'MA': 'MARKET',
        'MB': 'BET_CALL_V2_DISABLED, MAX_BET',
        'MC': 'CUSTOMER_TO_CUSTOMER_CALLING_FEATURE_DISABLED, COMMENT_V4, MARKET_COUNT',
        'MD': 'MATCHLIVE_PERIOD',
        'ME': 'MULTI_EVENT',
        'MF': 'MATCH_FLAG',
        'MG': 'MARKET_GROUP',
        'ML': 'MATCH_LENGTH',
        'MM': 'MERGE_MARKET',
        'MO': 'SECONDARY_UK_EVENT',
        'MP': 'MATCH_POSTPONED',
        'MR': 'CUSTOMER_TO_REPRESENTATIVE_CALLING_FEATURE_DISABLED, MORE_MARKETS',
        'MS': 'MEDIA_ID',
        'MT': 'BET_CALL_V2_TWILIO_DISABLED, MARKET_TYPE',
        'MU': 'MULTILINE',
        'MW': 'LOTTO_MAX_WINNINGS',
        'MY': 'MARKET_STYLE',
        'N2': 'NAME2',
        'NA': 'NAME',
        'NC': 'CLOTH_NUMBER',
        'NG': 'NGENERA',
        'NH': 'NEXT_HEADER',
        'NM': 'NON_MATCH_BASED',
        'NR': 'NON_RUNNER',
        'NT': 'NEUTRAL_VENUE_TEXT',
        'NV': 'NEUTRAL_VENUE',
        'OB': 'BANKER_OPTION, OPEN_BETS_ENABLED',
        'OD': 'ODDS',
        'OH': 'ODDS_HISTORY',
        'OO': 'ODDS_OVERRIDE',
        'OP': 'OPEN_BETS_PRESENTATION_PULL_DISABLED, OPEN_BETS',
        'OR': 'ORDER',
        'OT': 'OTHERS_AVAILABLE',
        'PA': 'PARTICIPANT',
        'PB': 'PUSH_BALANCE_ENABLED',
        'PC': 'PAGE_DATA_1, PARTICIPANT_COUNT, PARTIAL_CASHOUT_AVAILABLE',
        'PD': 'PAGE_DATA, POD, INFO_POD_TYPE, PULL_DELAY',
        'PE': 'PARTICIPANTS_EXCEEDED, PERIOD',
        'PF': 'PUSH_FLAG',
        'PG': 'PENALTY_GOALS, MATCHLIVE_ADDITIONAL_INFO, PAGE_TYPE',
        'PH': 'PHONE_ONLY',
        'PI': 'PLAYING_INDICATOR, AUS_TOTE_COMBINATION',
        'PN': 'CLOTH_NUMBER_PULL',
        'PO': 'POD_STACK_ORDER, POINTS',
        'PP': 'POD_OPEN',
        'PR': 'PREFERENCE_ID, MARKET_GROUP_USER_PREFERENCE',
        'PS': 'POD_STACK, PARTICIPANT_STATUS',
        'PT': 'PRODUCT_TYPE, POD_TYPE',
        'PV': 'PREMIUM_VERSION',
        'PX': 'NO_OFFER',
        'PY': 'PARTICIPANT_STYLE',
        'RA': 'RANGE',
        'RC': 'RESULT_CODE',
        'RD': 'RACE_DETAILS',
        'RE': 'BET_RETURNS',
        'RG': 'REGION',
        'RI': 'R4_COMMENT',
        'RO': 'DEFAULT_OPEN_RIGHT, RACE_OFF',
        'RS': 'RUNNER_STATUS, REGULAR_SINGLE',
        'RT': 'RESULTS_TEXT',
        'S1': 'MATCHLIVE_STATS_1',
        'S2': 'MATCHLIVE_STATS_2',
        'S3': 'MATCHLIVE_STATS_3',
        'S4': 'MATCHLIVE_STATS_4',
        'S5': 'MATCHLIVE_STATS_5',
        'S6': 'MATCHLIVE_STATS_6',
        'S7': 'MATCHLIVE_STATS_7',
        'S8': 'MATCHLIVE_STATS_8',
        'SA': 'CHANGE_STAMP, SUSPEND_ARRAY',
        'SB': 'SCOREBOARD_TYPE',
        'SC': 'SCORE, SCORES_COLUMN',
        'SD': 'AUDIO_ID',
        'SE': 'SECONDARY_EVENT',
        'SF': 'SPOTLIGHT_FORM',
        'SG': 'STAT_GROUP',
        'SI': 'IMAGE_ID_PULL, SECTION_ID',
        'SL': 'SCORES_CELL',
        'SM': 'START_TIME',
        'SN': 'DRAW_NUMBER_PULL',
        'SP': 'STAT_PERIOD',
        'SS': 'SHORT_SCORE, SUSPENDED_SELECTION',
        'ST': 'INFO_POD_DETAIL_1, STAT, POD_BODY_TEXT_1, STAKE',
        'SU': 'SUCCESS, SUSPENDED',
        'SV': 'MATCHLIVE_AVAILABLE',
        'SY': 'STYLE',
        'SZ': 'STAT_LOCATION',
        'T1': 'C1_TABLE, MINI_DIARY_T1, TEXT_1',
        'T2': 'C2_TABLE, MINI_DIARY_T2, TEXT_2',
        'T3': 'MINI_DIARY_T3, TEXT_3',
        'T4': 'TEXT_4',
        'T5': 'TEXT_5',
        'TA': 'TIME_ADDED',
        'TB': 'BREADCRUMB_TRAIL',
        'TC': 'BET_TOTE_TYPE, TEAM_COLOR',
        'TD': 'COUNTDOWN, TAX_DETAILS',
        'TE': 'TEAM',
        'TG': 'TEAM_GROUP',
        'TI': 'TMR_SERVER',
        'TL': 'LEAGUE_TOPIC, TOPIC_LIST',
        'TM': 'STAT_TIME, TMR_MINS',
        'TN': 'TRAINER_NAME',
        'TO': 'EMPTY_TOPIC_ID, PHONE_ONLY_LIST',
        'TP': 'TIME_STAMP',
        'TR': 'TAX_RATE, TOPIC_REFERENCE',
        'TS': 'TMR_SECS, TOTE_NAMES',
        'TT': 'TMR_TICKING',
        'TU': 'TMR_UPDATED',
        'TX': 'TAX_METHOD, TOPIC_LIST_EXCLUSIONS',
        'UC': 'CURRENT_INFO_V4',
        'UF': 'UPDATE_FREQUENCY',
        'VA': 'VALUE',
        'VC': 'MATCHLIVE_ANIMATION',
        'VD': 'VIRTUAL_DATA',
        'VI': 'VIDEO_AVAILABLE',
        'VL': 'VISIBLE',
        'VR': 'VIRTUAL_RACE',
        'VS': 'VIDEO_STREAM',
        'WG': 'WIZE_GUY',
        'WM': 'WINNING_MARGIN',
        'XB': 'CHECK_BOX',
        'XC': 'EXCLUDE_COLUMN_NUMBERS',
        'XI': 'EXTRA_INFO_NODE, TEAM_MATCHTOTAL_QUOTE',
        'XL': 'CONTROLLER',
        'XP': 'SHORT_POINTS',
        'XT': 'EXTRA_TIME_LENGTH',
        'XY': 'MATCHLIVE_COORDINATES',
        'ZA': 'TIMEZONE_ADJUSTMENT',
        '_V': 'PADDOCK_VIDEO_AVAILABLE'
    }

    bwin_sport_ids = {
        '4': 'Football',
        '7': 'Basketball',
        '5': 'Tennis',
        '18': 'Volleyball',
        '16': 'Handball',
        '23': 'Baseball',
        '12': 'Ice Hockey',
        '33': 'Snooker',
        '11': 'American Football',
        '22': 'Cricket',
        '70': 'Futsal',
        '34': 'Darts',
        '56': 'Table Tennis',
        '44': 'Badminton',
        '32': 'Rugby Union',
        '31': 'Rugby League',
        '24': 'Boxing',
        '36': 'Aussie Rules',
        '6': 'Formula 1',
        '13': 'Golf',
        '40': 'Motorbikes',
        '10': 'Cycling',
        '9': 'Alpine Skiing',
        '64': 'Biathlon',
        '100': 'E-Sports'
    }

    betfair_event_type_ids = {
        '1': 'Football',
        '7522': 'Basketball',
        '2': 'Tennis',
        '998917': 'Volleyball',
        '468328': 'Handball',
        '7524': 'Ice Hockey',
        '4': 'Cricket',
        '5': 'Rugby Union'
    }

    xbet_sport_ids = {
        '1': 'Football',
        '2': 'Ice Hockey',
        '3': 'Basketball',
        '6': 'Volleyball',
    }

    def __init__(self, token, session):
        self.api = f'https://api.b365api.com/ENDPOINT?token={token}'
        self.session = session
        self.r_countries = self.json_parser('https://betsapi.com/docs/samples/bet365_prematch_odds.json')

    async def get(self, api_url, lng_id):
        api_url += f'&LNG_ID={lng_id}' if lng_id else ''
        async with self.session.get(api_url) as response:
            return await response.json()

    async def in_play_events(self, sport_id, league_id='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v3/events/inplay') + f'&sport_id={sport_id}'
        api += f'&league_id={league_id}' if league_id else ''
        return await self.get(api, lng_id)

    async def upcoming_events(self, sport_id, league_id='', team_id='', cc='', day='', skip_esports='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v3/events/upcoming') + f'&sport_id={sport_id}'
        api += f'&league_id={league_id}' if league_id else ''
        api += f'&team_id={team_id}' if team_id else ''
        api += f'&cc={cc}' if cc else ''
        api += f'&day={day}' if day else ''
        api += f'&skip_esports={skip_esports}' if skip_esports else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def ended_events(self, sport_id, league_id='', team_id='', cc='', day='', skip_esports='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v3/events/ended') + f'&sport_id={sport_id}'
        api += f'&league_id={league_id}' if league_id else ''
        api += f'&team_id={team_id}' if team_id else ''
        api += f'&cc={cc}' if cc else ''
        api += f'&day={day}' if day else ''
        api += f'&skip_esports={skip_esports}' if skip_esports else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def events_search(self, sport_id, home, away, time, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/events/search') + f'&sport_id={sport_id}&home={home}&away={away}&time={time}'
        return await self.get(api, lng_id)

    async def event_view(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/event/view') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def event_history(self, event_id, qty='10', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/event/history') + f'&event_id={event_id}&qty={qty}'
        return await self.get(api, lng_id)

    async def event_odds_summary(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v2/event/odds/summary') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def event_odds(self, event_id, source='', since_time='', odds_market='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v2/event/odds') + f'&event_id={event_id}'
        api += f'&source={source}' if source else ''
        api += f'&since_time={since_time}' if since_time else ''
        api += f'&odds_market={odds_market}' if odds_market else ''
        return await self.get(api, lng_id)

    async def event_stats_trend(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/event/stats_trend') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def event_lineup(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/event/lineup') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def league(self, sport_id, cc='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/league') + f'&sport_id={sport_id}'
        api += f'&cc={cc}' if cc else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def league_table(self, league_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v2/league/table') + f'&league_id={league_id}'
        return await self.get(api, lng_id)

    async def league_toplist(self, league_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/league/toplist') + f'&league_id={league_id}'
        return await self.get(api, lng_id)

    async def team(self, sport_id, cc='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/team') + f'&sport_id={sport_id}'
        api += f'&cc={cc}' if cc else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def team_squad(self, team_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/team/squad') + f'&team_id={team_id}'
        return await self.get(api, lng_id)

    async def team_members(self, team_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/team/members') + f'&team_id={team_id}'
        return await self.get(api, lng_id)

    async def player(self, player_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/player') + f'&player_id={player_id}'
        return await self.get(api, lng_id)

    async def tennis_ranking(self, type_id='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/tennis/ranking')
        api += f'&type_id={type_id}' if type_id else ''
        return await self.get(api, lng_id)

    async def merge_history(self, since_time='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/event/merge_history')
        api += f'&since_time={since_time}' if since_time else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def bet365_in_play(self, raw='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bet365/inplay')
        api += f'&raw={raw}' if raw else ''
        return await self.get(api, lng_id)

    async def bet365_in_play_filter(self, sport_id='', league_id='', skip_esports='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bet365/inplay_filter')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&league_id={league_id}' if league_id else ''
        api += f'&skip_esports={skip_esports}' if skip_esports else ''
        return await self.get(api, lng_id)

    async def bet365_in_play_event(self, FI, stats='', lineup='', raw='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bet365/event') + f'&FI={FI}'
        api += f'&stats={statst_id}' if stats else ''
        api += f'&lineup={lineup}' if lineup else ''
        api += f'&raw={raw}' if raw else ''
        return await self.get(api, lng_id)

    async def bet365_upcoming_events(self, sport_id, league_id='', skip_esports='', day='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bet365/upcoming') + f'&sport_id={sport_id}'
        api += f'&league_id={league_id}' if league_id else ''
        api += f'&skip_esports={skip_esports}' if skip_esports else ''
        api += f'&day={day}' if day else ''
        api += f'&sport_id={page}' if page else ''
        return await self.get(api, lng_id)

    async def bet365_pre_match_odds(self, FI, raw='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v3/bet365/prematch') + f'&FI={FI}'
        api += f'&raw={raw}' if raw else ''
        return await self.get(api, lng_id)

    async def bet365_result(self, event_id, raw='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bet365/result') + f'&event_id={event_id}'
        api += f'&raw={raw}' if raw else ''
        return await self.get(api, lng_id)

    async def bwin_in_play(self, sport_id='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bwin/inplay')
        api += f'&sport_id={sport_id}' if sport_id else ''
        return await self.get(api, lng_id)

    async def bwin_event(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bwin/event') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def bwin_pre_match_odds(self, day='', sport_id='', league_id='', skip_markets='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bwin/prematch')
        api += f'&day={day}' if day else ''
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&league_id={league_id}' if league_id else ''
        api += f'&skip_markets={skip_markets}' if skip_markets else ''
        return await self.get(api, lng_id)

    async def bwin_result(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/bwin/result') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def betfair_sports_book_in_play(self, sport_id='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/sb/inplay')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def betfair_sports_book_upcoming(self, sport_id='', day='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/sb/upcoming')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&day={day}' if day else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def betfair_sports_book_event(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/sb/event') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def betfair_exchange_in_play(self, sport_id='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/ex/inplay')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def betfair_exchange_upcoming(self, sport_id='', day='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/ex/upcoming')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&day={day}' if day else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def betfair_exchange_event(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/ex/event') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def betfair_timeline(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/timeline') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def betfair_result(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betfair/result') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def sbobet_in_play(self, sport_id='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/sbobet/inplay')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def sbobet_upcoming(self, sport_id='', day='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/sbobet/upcoming')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&day={day}' if day else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def sbobet_event(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/sbobet/event') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def sbobet_result(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/sbobet/result') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def xbet_in_play(self, sport_id='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/1xbet/inplay')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def xbet_upcoming(self, sport_id='', day='', page='', lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/1xbet/upcoming')
        api += f'&sport_id={sport_id}' if sport_id else ''
        api += f'&day={day}' if day else ''
        api += f'&page={page}' if page else ''
        return await self.get(api, lng_id)

    async def xbet_event(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/1xbet/event') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def xbet_result(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/1xbet/result') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def william_hill_result(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/williamhill/result') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def betsson_result(self, event_id, lng_id=''):
        api = self.api.replace('ENDPOINT', 'v1/betsson/result') + f'&event_id={event_id}'
        return await self.get(api, lng_id)

    async def json_parser(self, url):
        async with self.session.get(url) as get:
            return await get.json()


class BetsAPISamples:

    def __init__(self, session):
        self.session = session
        self.in_play_events = self.json_parser('https://betsapi.com/docs/samples/inplay.json')
        self.upcoming_events = self.json_parser('https://betsapi.com/docs/samples/upcoming.json')
        self.ended_event = self.json_parser('https://betsapi.com/docs/samples/ended.json')
        self.search_event = self.json_parser('https://betsapi.com/docs/samples/search.json')
        self.event_view = self.json_parser('https://betsapi.com/docs/samples/event_view.json')
        self.event_history = self.json_parser('https://betsapi.com/docs/samples/event_history.json')
        self.event_odds_summary = self.json_parser('https://betsapi.com/docs/samples/event_odds_summary.json')
        self.event_odds = self.json_parser('https://betsapi.com/docs/samples/event_odds.json')
        self.event_stats_trend = self.json_parser('https://betsapi.com/docs/samples/event_stats_trend.json')
        self.event_lineup = self.json_parser('https://betsapi.com/docs/samples/event_lineup.json')
        self.league = self.json_parser('https://betsapi.com/docs/samples/league.json')
        self.league_table = self.json_parser('https://betsapi.com/docs/samples/league_table.json')
        self.league_toplist = self.json_parser('https://betsapi.com/docs/samples/league_toplist.json')
        self.team = self.json_parser('https://betsapi.com/docs/samples/team.json')
        self.team_squad = self.json_parser('https://betsapi.com/docs/samples/team_squad.json')
        self.team_members = self.json_parser('https://betsapi.com/docs/samples/team_members.json')
        self.player = self.json_parser('https://betsapi.com/docs/samples/player.json')
        self.tennis_ranking = self.json_parser('https://betsapi.com/docs/samples/tennis_ranking.json')
        self.merge_history = self.json_parser('https://betsapi.com/docs/samples/merge_history.json')
        self.bet365_in_play = self.json_parser('https://betsapi.com/docs/samples/bet365_inplay.json')
        self.bet365_in_play_filter = self.json_parser('https://betsapi.com/docs/samples/bet365_inplay_filter.json')
        self.bet365_in_play_event = self.json_parser('https://betsapi.com/docs/samples/bet365_event.soccer.json')
        self.bet365_upcoming_events = self.json_parser('https://betsapi.com/docs/samples/bet365_upcoming.json')
        self.bet365_pre_match_odds = self.json_parser('https://betsapi.com/docs/samples/bet365_prematch_odds.json')
        self.bet365_result = self.json_parser('https://betsapi.com/docs/samples/bet365_result.json')
        self.bwin_in_play = self.json_parser('https://betsapi.com/docs/samples/bwin_inplay.json')
        self.bwin_event = self.json_parser('https://betsapi.com/docs/samples/bwin_event.json')
        self.bwin_pre_match_odds = self.json_parser('https://betsapi.com/docs/samples/bwin_prematch.json')
        self.bwin_result = self.json_parser('https://betsapi.com/docs/samples/bwin_result.json')
        self.betfair_sports_book_in_play = self.json_parser('https://betsapi.com/docs/samples/betfair_sb_inplay.json')
        self.betfair_sports_book_upcoming = self.json_parser('https://betsapi.com/docs/samples/betfair_sb_upcoming.json')
        self.betfair_sports_book_event = self.json_parser('https://betsapi.com/docs/samples/betfair_sb_event.json')
        self.betfair_exchange_in_play = self.json_parser('https://betsapi.com/docs/samples/betfair_ex_inplay.json')
        self.betfair_exchange_upcoming = self.json_parser('https://betsapi.com/docs/samples/betfair_ex_upcoming.json')
        self.betfair_exchange_event = self.json_parser('https://betsapi.com/docs/samples/betfair_ex_event.json')
        self.betfair_timeline = self.json_parser('https://betsapi.com/docs/samples/betfair_timeline.json')
        self.betfair_result = self.json_parser('https://betsapi.com/docs/samples/betfair_result.json')
        self.sbobet_in_play = self.json_parser('https://betsapi.com/docs/samples/sbobet_inplay.json')
        self.sbobet_upcoming = self.json_parser('https://betsapi.com/docs/samples/sbobet_upcoming.json')
        self.sbobet_event = self.json_parser('https://betsapi.com/docs/samples/sbobet_event.json')
        self.sbobet_result = self.json_parser('https://betsapi.com/docs/samples/sbobet_result.json')
        self.xbet_in_play = self.json_parser('https://betsapi.com/docs/samples/1xbet_inplay.json')
        self.xbet_upcoming = self.json_parser('https://betsapi.com/docs/samples/1xbet_upcoming.json')
        self.xbet_event = self.json_parser('https://betsapi.com/docs/samples/1xbet_event.json')
        self.xbet_result = self.json_parser('https://betsapi.com/docs/samples/1xbet_result.json')
        self.william_hill_result = self.json_parser('https://betsapi.com/docs/samples/williamhill_result.json')
        self.betsson_result = self.json_parser('https://betsapi.com/docs/samples/sbobet_result.json')

    async def json_parser(self, url):
        async with self.session.get(url) as get:
            return await get.json()





