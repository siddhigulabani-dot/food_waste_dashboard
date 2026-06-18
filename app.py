import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(
    page_title="Food Waste Management Dashboard",
    page_icon="🍲",
    layout="wide"
)

st.title("Food Waste Management Dashboard")
st.markdown("Analysis of food donations, claims, providers and receivers")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Food Waste Management System", layout="wide")

st.title("🍽️ Food Waste Management System")

page = st.sidebar.selectbox(
    "Choose Data",
    ["Home", "Providers", "Receivers", "Food Listings", "Claims"]
)

if page == "Home":
    st.header("Welcome")
    st.write("Food Waste Management Dashboard")

elif page == "Providers":
    st.header("Providers Data")
    df = pd.read_csv("providers_data_cleaned.csv")
    st.dataframe(df)

elif page == "Receivers":
    st.header("Receivers Data")
    df = pd.read_csv("receivers_data_cleaned.csv")
    st.dataframe(df)

elif page == "Food Listings":
    st.header("Food Listings Data")
    df = pd.read_csv("food_listings_cleaned.csv")
    st.dataframe(df)

elif page == "Claims":
    st.header("Claims Data")
    df = pd.read_csv("claims_data_cleaned.csv")
    st.dataframe(df)

    import streamlit as st
import pandas as pd
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)

cursor = conn.cursor()

if conn.is_connected():
    st.success("✅ Connected to MySQL Database")


import streamlit as st
import pandas as pd
import mysql.connector

st.title("Food Waste Management Dashboard")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)

# Query 1 - Providers by City
query1 = """
SELECT City, COUNT(*) AS Total_Providers
FROM providers_data_cleaned
GROUP BY City;
"""

df1 = pd.read_sql(query1, conn)

st.subheader("Providers in Each City")
st.dataframe(df1)

st.bar_chart(df1.set_index("City"))  

import streamlit as st
import pandas as pd
import mysql.connector

st.title("Food Waste Management Dashboard")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)

    # Query 2 - Receivers by City
query2 = """
SELECT City, COUNT(*) AS Total_Receivers
FROM receivers_data_cleaned
GROUP BY City;
"""

df2 = pd.read_sql(query2, conn)

st.subheader("Receivers in Each City")
st.dataframe(df2)
st.bar_chart(df2.set_index("City"))

import streamlit as st
import pandas as pd
import mysql.connector

st.title("Food Waste Management Dashboard")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)
# Query 3 - Food Contribution by Provider Type
query3 = """
SELECT Provider_Type,
       SUM(Quantity) AS Total_Food_Contributed
FROM food_listings_cleaned
GROUP BY Provider_Type
ORDER BY Total_Food_Contributed DESC;
"""

df3 = pd.read_sql(query3, conn)

st.subheader("Food Contribution by Provider Type")
st.dataframe(df3)
st.bar_chart(df3.set_index("Provider_Type"))

import streamlit as st
import pandas as pd
import mysql.connector

st.title("Food Waste Management Dashboard")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)

query4 = """
SELECT r.Name,
       COUNT(c.Claim_ID) AS Total_Claims
FROM receivers_data_cleaned r
JOIN claims_data_cleaned c
ON r.Receiver_ID = c.Receiver_ID
GROUP BY r.Receiver_ID, r.Name
ORDER BY Total_Claims DESC;
"""

df4 = pd.read_sql(query4, conn)

st.subheader("Receivers Who Claimed the Most Food")
st.dataframe(df4)

st.bar_chart(df4.set_index("Name"))

import streamlit as st
import pandas as pd
import mysql.connector

st.title("Food Waste Management Dashboard")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)
query5 = """
SELECT SUM(Quantity) AS Total_Food_Available
FROM food_listings_cleaned;
"""

df5 = pd.read_sql(query5, conn)

st.subheader("Total Food Available")
st.dataframe(df5)

st.metric(
    "Total Food Available",
    int(df5["Total_Food_Available"][0])
)

import streamlit as st
import pandas as pd
import mysql.connector

st.title("Food Waste Management Dashboard")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)
query6 = """
SELECT Location,
       COUNT(*) AS Total_Listings
FROM food_listings_cleaned
GROUP BY Location
ORDER BY Total_Listings DESC;
"""

df6 = pd.read_sql(query6, conn)

st.subheader("Food Listings by City")
st.dataframe(df6)

st.bar_chart(df6.set_index("Location"))
import streamlit as st
import pandas as pd
import mysql.connector

st.title("Food Waste Management Dashboard")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12122012@niyati",
    database="food_waste_management"
)
query7 = """
SELECT Food_Type,
       COUNT(*) AS Count_Food
FROM food_listings_cleaned
GROUP BY Food_Type
ORDER BY Count_Food DESC;
"""

df7 = pd.read_sql(query7, conn)

st.subheader("Most Common Food Types")
st.dataframe(df7)

st.bar_chart(df7.set_index("Food_Type"))

query8 = """
SELECT f.Food_Name,
       COUNT(c.Claim_ID) AS Total_Claims
FROM food_listings_cleaned f
JOIN claims_data_cleaned c
ON f.Food_ID = c.Food_ID
GROUP BY f.Food_ID, f.Food_Name
ORDER BY Total_Claims DESC;
"""

df8 = pd.read_sql(query8, conn)

st.subheader("Food Claims by Food Item")
st.dataframe(df8)

st.bar_chart(df8.set_index("Food_Name"))

query9 = """
SELECT p.Name,
       COUNT(c.Claim_ID) AS Successful_Claims
FROM providers_data_cleaned p
JOIN food_listings_cleaned f
ON p.Provider_ID = f.Provider_ID
JOIN claims_data_cleaned c
ON f.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY p.Provider_ID, p.Name
ORDER BY Successful_Claims DESC;
"""

df9 = pd.read_sql(query9, conn)

st.subheader("Providers with Highest Successful Claims")
st.dataframe(df9)

st.bar_chart(df9.set_index("Name"))

query10 = """
SELECT Status,
ROUND(COUNT(*) * 100.0 /
      (SELECT COUNT(*) FROM claims_data_cleaned),2)
AS Percentage
FROM claims_data_cleaned
GROUP BY Status;
"""

df10 = pd.read_sql(query10, conn)

st.subheader("Claim Status Distribution")
st.dataframe(df10)

st.bar_chart(df10.set_index("Status"))

query8 = """
SELECT f.Food_Name,
       COUNT(c.Claim_ID) AS Total_Claims
FROM food_listings_cleaned f
JOIN claims_data_cleaned c
ON f.Food_ID = c.Food_ID
GROUP BY f.Food_ID, f.Food_Name
ORDER BY Total_Claims DESC;
"""

df8 = pd.read_sql(query8, conn)

st.subheader("Food Claims by Food Item")
st.dataframe(df8)

st.bar_chart(df8.set_index("Food_Name"))

query9 = """
SELECT p.Name,
       COUNT(c.Claim_ID) AS Successful_Claims
FROM providers_data_cleaned p
JOIN food_listings_cleaned f
ON p.Provider_ID = f.Provider_ID
JOIN claims_data_cleaned c
ON f.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY p.Provider_ID, p.Name
ORDER BY Successful_Claims DESC;
"""

df9 = pd.read_sql(query9, conn)

st.subheader("Providers with Highest Successful Claims")
st.dataframe(df9)

st.bar_chart(df9.set_index("Name"))

query10 = """
SELECT Status,
       ROUND(COUNT(*) * 100.0 /
       (SELECT COUNT(*) FROM claims_data_cleaned), 2) AS Percentage
FROM claims_data_cleaned
GROUP BY Status;
"""

df10 = pd.read_sql(query10, conn)

st.subheader("Claim Status Distribution (%)")
st.dataframe(df10)

st.bar_chart(df10.set_index("Status"))

query11 = """
SELECT r.Name,
       AVG(f.Quantity) AS Average_Quantity_Claimed
FROM receivers_data_cleaned r
JOIN claims_data_cleaned c
ON r.Receiver_ID = c.Receiver_ID
JOIN food_listings_cleaned f
ON c.Food_ID = f.Food_ID
GROUP BY r.Receiver_ID, r.Name
ORDER BY Average_Quantity_Claimed DESC;
"""

df11 = pd.read_sql(query11, conn)

st.subheader("Average Quantity Claimed Per Receiver")
st.dataframe(df11)

st.bar_chart(df11.set_index("Name"))

query12 = """
SELECT f.Meal_Type,
       COUNT(c.Claim_ID) AS Total_Claims
FROM food_listings_cleaned f
JOIN claims_data_cleaned c
ON f.Food_ID = c.Food_ID
GROUP BY f.Meal_Type
ORDER BY Total_Claims DESC;
"""

df12 = pd.read_sql(query12, conn)

st.subheader("Most Claimed Meal Types")
st.dataframe(df12)

st.bar_chart(df12.set_index("Meal_Type"))

query13 = """
SELECT p.Name,
       SUM(f.Quantity) AS Total_Donated
FROM providers_data_cleaned p
JOIN food_listings_cleaned f
ON p.Provider_ID = f.Provider_ID
GROUP BY p.Provider_ID, p.Name
ORDER BY Total_Donated DESC;
"""

df13 = pd.read_sql(query13, conn)

st.subheader("Total Quantity Donated by Each Provider")
st.dataframe(df13)

st.bar_chart(df13.set_index("Name"))
