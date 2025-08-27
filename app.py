import streamlit as st
import folium
from streamlit_folium import st_folium

# -----------------------
# PAGE CONFIG ABS
# -----------------------
st.set_page_config(page_title="Faco Limited", page_icon="🖋️", layout="wide")

CONTACT = {
    "business": "Faco Limited",
    "phones": [
        {"label": "Main Line / WhatsApp", "display": "+234 703 927 3135", "e164": "2347039273135"},
        {"label": "Alt Line",             "display": "+234 808 212 2221", "e164": "2348082122221"},
    ],
    "whatsapp_e164": "2347039273135",
    "email": "aliyuauwal@gmail.com",
    "address": "Kano, Nigeria",
    "lat": 12.0000,
    "lon": 8.5000,
    "hours": {"Mon–Fri": "8:30–18:00", "Sat": "9:00–16:00", "Sun": "Closed"},
    "wa_catalog_url": "",
}

# -----------------------
# STYLING
# -----------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif !important;
        background: linear-gradient(120deg, #0D3B66 0%, #06BCC1 50%, #FAF0CA 100%) !important;
        background-attachment: fixed;
        position: relative;
    }

    /* Abstract gradient blobs */
    body::before, body::after {
        content: "";
        position: absolute;
        width: 600px;
        height: 600px;
        border-radius: 50%;
        filter: blur(180px);
        z-index: -1;
    }
    body::before {
        background: rgba(244, 211, 94, 0.25);  /* golden soft blob */
        top: -200px;
        left: -150px;
    }
    body::after {
        background: rgba(13, 59, 102, 0.35);  /* deep blue blob */
        bottom: -250px;
        right: -200px;
    }

    h1, h2, h3 {
        font-weight: 600 !important;
        color: #0D3B66 !important;
    }

    /* Abstract Header */
    .abstract-header {
        background: linear-gradient(135deg, #0D3B66, #144E82, #1C658C);
        color: white;
        padding: 3rem 2rem;
        border-radius: 0 0 40px 40px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
        text-align: center;
    }

    /* Section divider */
    .section-divider {
        width: 100%;
        height: 80px;
        background: linear-gradient(135deg, #0D3B66, #144E82);
        border-radius: 0 0 50% 50% / 20%;
        margin: 2rem 0;
    }

    /* Cards */
    .material-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all .3s ease-in-out;
    }
    .material-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    }

    /* WhatsApp Floating Button */
    .whatsapp-float {
        position: fixed;
        width: 60px; height: 60px;
        bottom: 20px; right: 20px;
        background: #25D366;
        color: white; border-radius: 50%;
        text-align: center;
        font-size: 32px; line-height: 60px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.25);
        z-index: 999;
        transition: transform .2s;
    }
    .whatsapp-float:hover {transform: scale(1.08);}
    </style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.markdown(f"""
    <div class="abstract-header">
        <img src="logo.png" width="100" style="margin-bottom:1rem;">
        <h1>{CONTACT['business']}</h1>
        <h3>Office Stationery & Student Supplies</h3>
    </div>
""", unsafe_allow_html=True)

# -----------------------
# PRODUCTS
# -----------------------
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.subheader("Our Products")
cols = st.columns(3)

products = [
    {"name": "Exercise Books", "desc": "Durable books for students", "price": "₦500"},
    {"name": "Pens & Pencils", "desc": "Quality writing instruments", "price": "₦100"},
    {"name": "Office Files", "desc": "Organize your work", "price": "₦300"},
    {"name": "A4 Paper", "desc": "500 sheets per pack", "price": "₦2,500"},
    {"name": "Markers", "desc": "Whiteboard & permanent markers", "price": "₦250"},
    {"name": "Calculators", "desc": "Scientific & basic calculators", "price": "₦2,000"},
]

for i, p in enumerate(products):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="material-card">
                <h4>{p['name']}</h4>
                <p>{p['desc']}</p>
                <strong>{p['price']}</strong>
            </div>
        """, unsafe_allow_html=True)

# -----------------------
# CONTACT SECTION
# -----------------------
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.subheader("📞 Contact Us")

c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="material-card">', unsafe_allow_html=True)
    st.markdown(f"**📍 Address:** {CONTACT['address']}")
    for ph in CONTACT["phones"]:
        st.markdown(f"**📞 {ph['label']}:** [{ph['display']}](tel:{ph['e164']})")
    st.markdown(f"**📧 Email:** [{CONTACT['email']}](mailto:{CONTACT['email']})")
    hours_str = "<br>".join([f"**{k}:** {v}" for k, v in CONTACT["hours"].items()])
    st.markdown(f"**🕒 Business Hours:** <br>{hours_str}", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="material-card">', unsafe_allow_html=True)
    st.markdown("**🌍 Find Us on Map:**")
    m = folium.Map(location=[CONTACT["lat"], CONTACT["lon"]], zoom_start=13)
    folium.Marker(
        [CONTACT["lat"], CONTACT["lon"]],
        tooltip=CONTACT["business"],
        popup=CONTACT["address"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)
    st_folium(m, width=350, height=250)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# WHATSAPP FLOAT
# -----------------------
prefilled_msg = f"Hello {CONTACT['business']}, I’d like to place an order."
wa_link = CONTACT["wa_catalog_url"] or f"https://wa.me/{CONTACT['whatsapp_e164']}?text={prefilled_msg.replace(' ', '%20')}"

st.markdown(f"""
    <a href="{wa_link}" class="whatsapp-float" target="_blank" title="Chat on WhatsApp">
        💬
    </a>
""", unsafe_allow_html=True)
