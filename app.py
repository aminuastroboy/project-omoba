import streamlit as st

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Faco Limited", page_icon="🖊️", layout="wide")

# =========================
# Custom CSS (Material Design Inspired)
# =========================
st.markdown("""
    <style>
        /* General font */
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }

        /* Hero section */
        .hero {
            position: relative;
            background-image: url('https://images.unsplash.com/photo-1524995997946-a1c2e315a42f');
            background-size: cover;
            background-position: center;
            height: 420px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            margin-bottom: 40px;
        }
        .hero-overlay {
            background-color: rgba(0,0,0,0.55);
            padding: 50px;
            border-radius: 20px;
        }
        .hero h1 {
            font-size: 2.7rem;
            font-weight: 700;
        }
        .hero p {
            font-size: 1.3rem;
        }
        .hero a {
            background-color: #2196F3;
            padding: 12px 25px;
            border-radius: 8px;
            text-decoration: none;
            color: white;
            font-weight: bold;
            display: inline-block;
            margin-top: 20px;
            box-shadow: 0px 3px 6px rgba(0,0,0,0.3);
            transition: 0.2s;
        }
        .hero a:hover {
            background-color: #1565C0;
        }

        /* Info cards */
        .info-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            transition: 0.2s;
        }
        .info-card:hover {
            box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
            transform: translateY(-3px);
        }
        .info-card h3 {
            color: #2196F3;
            margin-bottom: 10px;
        }

        /* Product grid */
        .product-card {
            background: #fff;
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            text-align: center;
            transition: 0.2s;
        }
        .product-card:hover {
            transform: translateY(-4px);
            box-shadow: 0px 6px 14px rgba(0,0,0,0.2);
        }
        .product-card img {
            border-radius: 12px;
            margin-bottom: 10px;
        }
        .product-card a {
            background-color: #2196F3;
            padding: 8px 18px;
            border-radius: 6px;
            color: white !important;
            text-decoration: none;
            font-weight: 500;
            display: inline-block;
            margin-top: 8px;
        }
        .product-card a:hover {
            background-color: #1565C0;
        }

        /* Floating WhatsApp button */
        .whatsapp-float {
            position: fixed;
            width: 60px;
            height: 60px;
            bottom: 20px;
            right: 20px;
            background-color: #25D366;
            color: #FFF;
            border-radius: 50px;
            text-align: center;
            font-size: 30px;
            box-shadow: 2px 2px 3px #999;
            z-index: 100;
        }
        .whatsapp-float:hover {
            background-color: #1EBE5D;
        }
        .whatsapp-icon {
            margin-top: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# Sidebar Menu
# =========================
menu = ["Home", "Products", "About Us", "Contact"]
choice = st.sidebar.radio("Navigate", menu)

# WhatsApp Number
WHATSAPP_NUMBER = "2347039273135"   # replace with real business number

# =========================
# Product Catalog
# =========================
products = [
    {"name": "Notebooks", "category": "School", 
     "img": "https://images.unsplash.com/photo-1589998059171-988d887df646"},
    {"name": "Pens & Markers", "category": "School", 
     "img": "https://images.unsplash.com/photo-1589190051288-0f9c1f24f7d4"},
    {"name": "Office Supplies", "category": "Office", 
     "img": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4"},
    {"name": "Calculators", "category": "School", 
     "img": "https://images.unsplash.com/photo-1581090700227-4c4d9b3c46a1"},
    {"name": "Files & Folders", "category": "Office", 
     "img": "https://images.unsplash.com/photo-1616627781961-c7eec2a3f8c4"},
]

# =========================
# Home
# =========================
if choice == "Home":
    # Hero Banner
    st.markdown("""
        <div class="hero">
            <div class="hero-overlay">
                <h1>Welcome to Faco Limited</h1>
                <p>Your one-stop shop for Office & School Supplies</p>
                <a href="#products">📦 Shop Now</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Info Highlights
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="info-card"><h3>🚚 Fast Delivery</h3><p>Quick & reliable to your doorstep.</p></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="info-card"><h3>💰 Best Prices</h3><p>Affordable for students & offices.</p></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="info-card"><h3>✅ Trusted Quality</h3><p>We only stock durable items.</p></div>""", unsafe_allow_html=True)

# =========================
# Products
# =========================
elif choice == "Products":
    st.header("🛒 Our Products")
    st.markdown('<a name="products"></a>', unsafe_allow_html=True)  # anchor

    # Search + Filter
    search = st.text_input("🔍 Search Products")
    category = st.selectbox("📂 Filter by Category", ["All", "School", "Office"])

    filtered_products = [
        p for p in products
        if (search.lower() in p["name"].lower()) and
           (category == "All" or p["category"] == category)
    ]

    # Display products as cards
    cols = st.columns(3)
    for i, product in enumerate(filtered_products):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{product['img']}" width="100%" />
                    <h4>{product['name']}</h4>
                    <a href="https://wa.me/2347039273135?text=Hello%20Faco%20Limited%2C%20I%20want%20to%20order%20{product['name']}" target="_blank">📩 Order on WhatsApp</a>
                </div>
            """, unsafe_allow_html=True)

# =========================
# About Us
# =========================
elif choice == "About Us":
    st.header("About Faco Limited")
    st.write("""
        **Faco Limited** is passionate about providing students and professionals 
        with the best stationery products. 
        From notebooks and pens to office essentials, we’ve got it all.
    """)

# =========================
# Contact
# =========================
elif choice == "Contact":
    st.header("📞 Contact Us")
    st.write("**Phone:** +234 703 927 3135")
    st.write(f"**WhatsApp:** [Chat with us](https://wa.me/2347039273135)")
    st.write("**Email:** aliyuauwal@gmail.com")
    st.map("lat": 9.2795, "lon": 12.4582)  # Example location (Kano, Nigeria)

# =========================
# Floating WhatsApp Button
# =========================
st.markdown(f"""
    <a href="https://wa.me/2347039273135?text=Hello%20Faco%20Limited%21%20I%20would%20like%20to%20make%20an%20inquiry" class="whatsapp-float" target="_blank">
        <i class="fa fa-whatsapp whatsapp-icon">💬</i>
    </a>
""", unsafe_allow_html=True)
