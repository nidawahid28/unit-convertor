# Project 01: Unit Convertor

import streamlit as st

st.set_page_config(
    page_title="Unit Converter",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .block-container {
            padding: 0rem;
            margin-top: -4rem;
        }
        .main {
            background-color: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
            margin: 1rem;
        }
        h1 {
            text-align: center;
            font-size: 2.5rem;
            color: #1e88e5;
            margin-bottom: 1.5rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .description {
            text-align: center;
            color: #666;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }
        .stButton>button {
            background: linear-gradient(45deg, #1e88e5, #1976d2);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 2rem;
            font-size: 1.1rem;
            font-weight: 600;
            width: 100%;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #1976d2, #1565c0);
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        }
        .stSelectbox {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            padding: 0.5rem;
        }
        .result-box {
            background: linear-gradient(135deg, #f8f9fa, #ffffff);
            font-size: 1.5rem;
            font-weight: 600;
            color: #1e88e5;
            text-align: center;
            margin-top: 2rem;
            padding: 1.5rem;
            border-radius: 15px;
            border: 2px solid rgba(30, 136, 229, 0.1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }
        .footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1rem;
            font-size: 0.9rem;
            color: #888;
            border-top: 1px solid #eee;
        }
        .stNumberInput {
            background-color: white;
            border-radius: 10px;
            padding: 0.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
            padding: 2rem 1rem;
            margin-top: -4rem;
        }
    </style>
""", unsafe_allow_html=True)

# Container for main content
st.markdown('<div class="main">', unsafe_allow_html=True)

# Title and description with emojis
st.markdown("<h1>🔄 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown('<p class="description">✨ A powerful tool to convert between different units of length, weight, and temperature with precision ✨</p>', unsafe_allow_html=True)

# Sidebar styling and content
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["📏 Length", "⚖️ Weight", "🌡️ Temperature"]
    )

# Strip the emoji from conversion type for processing
conversion_type = conversion_type.split()[1] if conversion_type else ""

# Main content
st.markdown("### 📝 Enter Values")
value = st.number_input("Enter the value to convert:", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From 📍", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    with col2:
        to_unit = st.selectbox("To 🎯", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
        
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From 📍", ["Kilograms", "Grams", "Pounds", "Ounces", "Milligrams"])
    with col2:
        to_unit = st.selectbox("To 🎯", ["Kilograms", "Grams", "Pounds", "Ounces", "Milligrams"])
    
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From 📍", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To 🎯", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_convertor(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]
    
def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274, "Milligrams": 1000000
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Button for conversion
if st.button("🔄 Convert Units"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)
        
    st.markdown(f"""<div class='result-box'>
        <div style='font-size: 1.1rem; color: #666; margin-bottom: 0.5rem'>🎉 Result:</div>
        {value:,.4f} {from_unit} ➡️ {result:,.4f} {to_unit}
        </div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close main container
    
st.markdown("""
    <div class='footer'>
        <div>Developed by Nida Wahid Baig</div>
        <div style='font-size: 0.8rem; margin-top: 0.5rem; color: #aaa;'></div>
    </div>
""", unsafe_allow_html=True)


    
    
        


