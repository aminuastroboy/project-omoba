import streamlit as st
import pandas as pd
import urllib.parse

# ======================================
# Config
# ======================================
st.set_page_config(page_title="Faco Limited", page_icon="🖊️", layout="wide")

WHATSAPP_NUMBER = "2347039273135"

# ======================================
# Custom CSS (Material Design Inspired)
# ======================================
st.markdown("""
<style>
    body {font-family: 'Roboto', sans-serif;}

    /* Navigation Bar */
    .navbar {
        background: linear-gradient(90deg, #1976d2, #42a5f5);
        padding: 12px 20px;
        color: white;
        font-size: 18px;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .navbar a {
        text-decoration: none;
        color: white;
        margin: 0 10px;
    }
    .navbar a:hover {
        text-decoration: underline;
    }

    /* Hero */
    .hero {
        background: linear-gradient(135deg, #42a5f5, #1976d2);
        padding: 60px 20px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    .hero h1 {font-size: 2.5rem; font-weight: bold;}
    .hero p {font-size: 1.2rem;}

    /* Product Card */
    .product-card {
        background: #fff;
        border-radius: 16px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
    }
    .product-card:hover {transform: translateY(-5px);}
    .product-card img {border-radius: 12px; margin-bottom: 10px;}
    .product-card h4 {margin: 5px 0; color: #1976d2;}

    /* Floating WhatsApp Button */
    .whatsapp-float {
        position: fixed;
        width: 60px;
        height: 60px;
        bottom: 20px;
        right: 20px;
        background-color: #25d366;
        color: #FFF;
        border-radius: 50px;
        text-align: center;
        font-size: 30px;
        box-shadow: 2px 2px 3px #999;
        z-index: 100;
    }
    .whatsapp-float i {
        margin-top: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ======================================
# Navbar
# ======================================
st.markdown("""
<div class="navbar">
    <div>🖊️ Faco Limited</div>
    <div>
        <a href="#home">Home</a>
        <a href="#products">Products</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================================
# Hero Section
# ======================================
st.markdown("""
<div id="home" class="hero">
    <h1>Welcome to Faco Limited</h1>
    <p>Your one-stop shop for Office & School Supplies</p>
    <a href="#products"><button style="padding:12px 24px; border:none; border-radius:8px; background:#fff; color:#1976d2; font-weight:bold; cursor:pointer;">Shop Now</button></a>
</div>
""", unsafe_allow_html=True)

# ======================================
# Product Catalog
# ======================================
products = [
    {"name": "Notebooks", "category": "School", "img": "https://images.unsplash.com/photo-1589998059171-988d887df646"},
    {"name": "Pens & Markers", "category": "School", "img": "https://images.unsplash.com/photo-1589190051288-0f9c1f24f7d4"},
    {"name": "Office Supplies", "category": "Office", "img": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4"},
    {"name": "Calculators", "category": "School", "img": "https://images.unsplash.com/photo-1581090700227-4c4d9b3c46a1"},
    {"name": "Files & Folders", "category": "Office", "img": "https://images.unsplash.com/photo-1616627781961-c7eec2a3f8c4"},
]

st.markdown('<div id="products"></div>', unsafe_allow_html=True)
st.subheader("🛒 Our Products")

search = st.text_input("🔍 Search Products")
category = st.selectbox("📂 Filter by Category", ["All", "School", "Office"])

filtered = [
    p for p in products
    if search.lower() in p["name"].lower() and (category == "All" or p["category"] == category)
]

cols = st.columns(3)
for i, product in enumerate(filtered):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <img src="{product['img']}" width="100%">
            <h4>{product['name']}</h4>
        </div>
        """, unsafe_allow_html=True)
        with st.form(key=f"order_{i}"):
            name = st.text_input("Your Name", key=f"name_{i}")
            submit = st.form_submit_button("📩 Order on WhatsApp")
            if submit and name.strip():
                msg = f"Hello Faco Limited, my name is {name}. I want to order {product['name']}."
                encoded = urllib.parse.quote(msg)
                url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded}"
                st.markdown(f"[👉 Click here to send WhatsApp message]({url})", unsafe_allow_html=True)

# ======================================
# About Section
# ======================================
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.subheader("ℹ️ About Us")
st.write("""
Faco Limited is passionate about providing students and professionals with the best stationery products. 
From notebooks and pens to office essentials, we’ve got it all — at affordable prices with fast delivery.
""")

# ======================================
# Contact Section
# ======================================
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.subheader("📞 Contact Us")
st.write("**Phone:** +234 703 927 3135")
st.write(f"**WhatsApp:** [Chat with us](https://wa.me/{WHATSAPP_NUMBER})")
st.write("**Email:** aliyuauwal@gmail.com")

location = pd.DataFrame({'lat': [9.2795], 'lon': [12.4582]})
st.map(location, zoom=12)

# ======================================
# Floating WhatsApp Button
# ======================================
st.markdown(f"""
<a href="https://wa.me/{WHATSAPP_NUMBER}" class="whatsapp-float" target="_blank">
    <i class="fa fa-whatsapp"></i>
</a>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
""", unsafe_allow_html=True)
