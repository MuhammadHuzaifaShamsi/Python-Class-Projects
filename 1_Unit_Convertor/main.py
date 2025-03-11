import streamlit as st

st.set_page_config(page_title="HUX - Unit Converter")

st.title("🌎 HUX - Unit Converter")

def length_converter(value, from_unit, to_unit):
    units = {
        "m": 1, "km": 1000, "feet": 0.3048, "inch": 0.0254, "cm": 0.01, "miles": 1609.34
    }
    return value * (units[from_unit] / units[to_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "F" and to_unit == "K":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32
    return value

def time_converter(value, from_unit, to_unit):
    units = {
        "seconds": 1, "minutes": 60, "hours": 3600, "days": 86400, 
        "months": 2.628e+6, "years": 3.154e+7
    }
    return value * (units[from_unit] / units[to_unit])

def mass_converter(value, from_unit, to_unit):
    units = {
        "kg": 1, "g": 1000, "pounds": 2.20462, "mg": 1e+6, "tonne": 0.001
    }
    return value * (units[from_unit] / units[to_unit])


st.subheader("🛠 Select Conversion Type:")
conversion_types = ["Length", "Temperature", "Time", "Mass"]
selected_type = st.radio("Choose a category:", conversion_types)

unit_options = {
    "Length": ["m", "km", "feet", "inch", "cm", "miles"],
    "Temperature": ["C", "F", "K"],
    "Time": ["seconds", "minutes", "hours", "days", "months", "years"],
    "Mass": ["kg", "g", "pounds", "mg", "tonne"]
}

from_unit = st.selectbox("Convert from:", unit_options[selected_type])
to_unit = st.selectbox("Convert to:", unit_options[selected_type])

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    if selected_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif selected_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif selected_type == "Time":
        result = time_converter(value, from_unit, to_unit)
    elif selected_type == "Mass":
        result = mass_converter(value, from_unit, to_unit)

    st.success(f"{value} {from_unit} is {result:.2f} {to_unit}")

