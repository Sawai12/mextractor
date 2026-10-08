from pyrogram.types import InlineKeyboardButton as KB, InlineKeyboardMarkup as KM
import msg, random, standardb
from modules import appxfree


async def get_appx_api():
    return await standardb.db_instance.get_appx_api()

app_identifier_map = {}

async def gen_apps_free_kb(page=0, apps_per_page=25):
    APPX_API = await get_appx_api()
    start = page * apps_per_page
    end = start + apps_per_page
    paginated_apps = list(APPX_API.items())[start:end]
    keys = []
    for idx, (app, api) in enumerate(paginated_apps):
        unique_id = f"{page}_{idx}"
        app_identifier_map[unique_id] = (app, api)
        keys.append(KB(f"🚀 {app} 🆕", callback_data=f"free_{unique_id}"))
    keyboard = [keys[i:i + 2] for i in range(0, len(keys), 2)]
    nav_buttons = []
    if start > 0:
        nav_buttons.append(KB("⬅️Back⬅️", callback_data=f"previous_{page - 1}"))
    if end < len(APPX_API):
        nav_buttons.append(KB("➡️Next➡️", callback_data=f"forward_{page + 1}"))
    nav_buttons.append(KB("🔰Menu🔰", callback_data="home"))
    nav_buttons.append(KB("❌Close❌", callback_data="close"))
    keyboard.append(nav_buttons)
    return KM(keyboard), page + 1, (len(APPX_API) + apps_per_page - 1) // apps_per_page

async def handle_app(bot, data, call_msg, a):
    try:
        app_id = "_".join(data.split('_')[1:])
    except IndexError:
        await a("Error: Unable to extract app_id from data..Please start it by /app")
        return
    app_details = app_identifier_map.get(app_id)
    if app_details is None:
        await a(f"Error: app_id {app_id} not found in app_identifier_map..Restart Markup Keyboard by /app")
        return
    app_name, api = app_details
    await a(f"You have Selected: {app_name}, API: {api}", show_alert=True)
    await call_msg.delete()
    await appxfree.handle_appx_free(bot, call_msg, app_name, api)

async def appx_page(call_msg, page):
    markup, current_page, total_pages = await gen_apps_free_kb(page)
    caption = f"{msg.APP}\n<b>Current page: </b>{current_page}/{total_pages}"
    await call_msg.edit_caption(caption=caption, reply_markup=markup)

def gen_app_kb(page):
    if page == 1:
        keyboard = [
            [KB("🌐 All Appx API APP [Web Url or API] 🌐", callback_data="master")],
            [KB("📱 All ClassPlus APK 📱", callback_data="cp")],
            [KB("🔑 ClassPlus Token Generator 🔑", callback_data="token")],
            [KB("📘 Edukemy 📘", callback_data="edukemy"), KB("📗 Apni Kaksha 📗", callback_data="kaksha")],
            [KB("📕 Khan GS 📕", callback_data="khan")],
            [KB("📙 Neon Classes 📙", callback_data="neon")],
            [KB("🎓 Nidhi Academy 🎓", callback_data="nidhi"), KB("🎥 KD LIVE 🎥", callback_data="kd")],
            [KB("📚 Physics Wallah 📚", callback_data="pw")],
            [KB("👨‍🏫 Tarun Grover Sir 👨‍🏫", callback_data="tarun")],
            [KB("🏫 My Pathsala 🏫", callback_data="path"), KB("📝 TestBook 📝", callback_data="kd")],
            [KB("🌟 My Rising India 🌟", callback_data="rising")],
            [KB("🩺 Nursing Next 🩺", callback_data="nursing")],
            [KB("⏩ Next Page ➡️", callback_data="ext_page_1")]
        ]
    elif page == 2:
        keyboard = [
            [KB("🎯 Allen New V2 🎯", callback_data="allenv2")],
            [KB("🚀 Allen Institute 🚀", callback_data="allen")],
            [KB("🎓 IFAS Academy 🎓", callback_data="ifas"), KB("🧑‍🏫 ICS Coaching 🧑‍🏫", callback_data="ics")],
            [KB("🌟 Sanskriti IAS 🌟", callback_data="rising")],
            [KB("🩺 Nursing Next 🩺", callback_data="nursing")],
            [KB("💡 Study IQ 💡", callback_data="iq"), KB("🏆 Utkarsh 🏆", callback_data="utk")],
            [KB("📚 Forum IAS 📚", callback_data="forum")],
            [KB("🔍 Vision IAS 🔍", callback_data="vision")],
            [KB("💼 Insight IAS 💼", callback_data="insight"), KB("📝 Vajiram IAS 📝", callback_data="vajiram")],
            [KB("🔑 Sunya IAS 🔑", callback_data="sunya")],
            [KB("📈 Level UP IAS 📈", callback_data="level")],
            [KB("🏅 Next IAS 🏅", callback_data="next"), KB("🔧 MadeEasy 🔧", callback_data="madeeasy")],
            [KB("🌐 WebSankul 🌐", callback_data="webs")],
            [KB("💻 All Spayee Websites 💻", callback_data="spayee")],
            [KB("💻 DSL KrantiKari 💻", callback_data="dsl")],
            [KB("🔙 Back Page ⬅️", callback_data="ack_page_2"), KB("🏠 Home 🏠", callback_data="home"), KB("➡️ Next Page ➡️", callback_data="ext_page_2")]
        ]
    elif page == 3:
        keyboard = [
            [KB("🌐 Appx All API (Nothing Required) 🌐", callback_data="appxfree")],
            [KB("🎲 Adda 247 (Any Random Login) 🎲", callback_data="addafree")],
            [KB("📘 Abhinav Maths (Nothing Required) 📘", callback_data="abhinavfree")],
            [KB("🚀 CDS Journey (Any Random Login) 🚀", callback_data="cdsfree")],
            [KB("📱 ClassPlus (Org Code Required) 📱", callback_data="cpfree")],
            [KB("🎓 Awadh Ojha App (Nothing Required) 🎓", callback_data="awadhfree")],
            [KB("📕 Khan Sir (Nothing Required) 📕", callback_data="khanfree")],
            [KB("🧑‍🏫 ICS Coaching (Any Random Login) 🧑‍🏫", callback_data="icsfree")],
            [KB("🧑‍🏫 IFAS Academy (Any Random Login) 🧑‍🏫", callback_data="ifasfree")],
            [KB("📚 Forum IAS (Any Random Token) 📚", callback_data="forumfree")],
            [KB("📚 JRF Adda (Nothing Required) 📚", callback_data="jrffree")],
            [KB("🏫 My Pathsala (Nothing Required) 🏫", callback_data="pathsalafree")],
            [KB("🔑 Physics Wallah (Any Random Token) 🔑", callback_data="pwfree")],
            [KB("🎓 Quality Education (Nothing Required) 🎓", callback_data="qualityfree")],
            [KB("💡 Study IQ (Nothing Required) 💡", callback_data="iqfree")],
            [KB("📘 Sunya IAS (Nothing Required) 📘", callback_data="sunyafree")],
            [KB("📝 Test Paper (Nothing Required) 📝", callback_data="testpaperlivefree")],
            [KB("🎯 TestBook (Any Random Login) 🎯", callback_data="testbookfree")],
            [KB("🚀 Verbal Math (Nothing Required)🚀 ", callback_data="verbalfree")],
            [KB("🔙 Back Page ⬅️", callback_data="ack_page_3"), KB("❌ Close ❌", callback_data="close"), KB("🏠 Home 🏠", callback_data="home")]
        ]
    return KM(keyboard)


def contact():
    keyboard = [[KB("📍 Contact Admin 📍", url="https://t.me/TgXMaster")]]
    return KM(keyboard)

def join_user():
    keyboard = KM([[KB("✨ Join Our Channel ✨", url="https://t.me/+xK5l5hnHvwI1MDlh")]])
    return keyboard

def home():
    keyboard = [
        [KB("🌟 VIP (Normal App) 🤖", callback_data="page_1"), KB("🚀 PRO (Special App) 🚀", callback_data="page_2")],
        [KB("⚡ Legend (No Login Required) ⚡", callback_data="page_3")],
        [KB("❌ Close ❌", callback_data="close")]
    ]
    return KM(keyboard)


async def send_random_photo(): 
    width = random.randint(1150, 1250)
    height = random.randint(700, 800)
    return f"https://picsum.photos/{width}/{height}.jpg"