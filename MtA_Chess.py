import streamlit as st
import pandas as pd

# IMAGE
st.image("MACC_LOGO_CROPPED.png")

# TITLE, TIME AND PLACE
st.markdown("""
<h1 style="background: linear-gradient(to right, #892432, #B89112); 
            -webkit-background-clip: text; 
            color: transparent;">
    Mount Allison University 2024 Open Chess Tournament
</h1>
""", unsafe_allow_html=True)



st.markdown('Location: Mount Allison University Chapel, *York St, Sackville, NB E4L 1A6*')
st.text('Time: TBA')
st.text('Date: TBA')
st.caption('Stay Tuned! We will be posting more information soon!')


# TOURNAMENT & REGISTERATION
st.header('Tournament Details')
link = 'https://docs.google.com/forms/d/1IzIGxOUs6xwF0eYROE1mtyBCNxnL4b39_wV59A06LyE/edit'
st.markdown('#### [**Register Here**](%s)' % link)


# ACCOMODATION
st.header('Accomodation Options in Sackville')
df = pd.DataFrame(
  [
      {"Location": "Sackville (NB)", "Hotel Name": "Coastal Inn", "Price": 144, "Google Maps Link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d44427.751587534156!2d-64.41360843287423!3d45.896623399999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4b5f50b9116b0349%3A0x7858c11ee555acfd!2sCoastal%20Inn%20Sackville!5e0!3m2!1sen!2sca!4v1676488725627!5m2!1sen!2sca"},
      {"Location": "Sackville (NB)", "Hotel Name": "Marshlands Inn", "Price": 103, "Google Maps Link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d44427.751587534156!2d-64.41360843287423!3d45.896623399999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4b5f50ee6ded1833%3A0xbc4c5439667f0a15!2sMarshlands%20Inn!5e0!3m2!1sen!2sca!4v1676488819647!5m2!1sen!2sca"},
      {"Location": "Sackville (NB)", "Hotel Name": "Tantramar Motel", "Price": 129, "Google Maps Link": "https://www.google.com/maps/place/Tantramar+Motel/@45.8966234,-64.4136084,13z/data=!4m11!3m10!1s0x4b5f50f5bed0c3eb:0x885fc9fb15c047f4!5m3!1s2023-03-18!4m1!1i2!8m2!3d45.8958193!4d-64.3497037!15sCgZIb3RlbHNaCCIGaG90ZWxzkgEFbW90ZWzgAQA!16s%2Fg%2F1tqnl6dq?coh=164777&entry=tt"},
      {"Location": "Amherst (NS)", "Hotel Name": "Wandlyn Inn", "Price": 126, "Google Maps Link": "https://www.google.com/maps/place/Wandlyn+Inn+Amherst/@45.8945327,-64.3835677,12z/data=!4m11!3m10!1s0x4b5f4eae9d1f75b1:0x7e985c915f9e553b!5m3!1s2023-03-18!4m1!1i2!8m2!3d45.8189152!4d-64.2364168!15sCgZIb3RlbHNaCCIGaG90ZWxzkgEFaG90ZWyaASNDaFpEU1VoTk1HOW5TMFZKUTBGblNVTlZPRFpFWDBsM0VBReABAA!16s%2Fg%2F1vd94pdf?coh=164777&entry=tt"},
      {"Location": "Amherst (NS)", "Hotel Name": "Comfort Inn", "Price": 139, "Google Maps Link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d88858.84858221447!2d-64.38356769034924!3d45.894532659331944!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4b5f494377af3ea5%3A0xad4358dbc86e1cc4!2sComfort%20Inn!5e0!3m2!1sen!2sca!4v1676489172038!5m2!1sen!2sca"},
      {"Location": "Amherst (NS)", "Hotel Name": "Super 8 by Wyndham", "Price": 141, "Google Maps Link": "https://goo.gl/maps/isZ6Ed58APbx9ci5A"},
  ]
)
edited_df = st.data_editor(df)



# FOOD
st.header('Food Options in Sackville')

df = pd.DataFrame(
    [
        {"Food Option": "Fener's Place", "Organizer Rating": 4.6, "Google Maps Link": "https://maps.app.goo.gl/Ba7o8SBEYZ8o7vHZ7"},
        {"Food Option": "Oh Chicken", "Organizer Rating": 4.7, "Google Maps Link": "https://maps.app.goo.gl/2zztLNeiAL7dW1LF7"},
        {"Food Option": "Song's Chopsticks", "Organizer Rating": 4.5, "Google Maps Link": "https://maps.app.goo.gl/SAqPBs1APLUmxvae6"},
        {"Food Option": "Goya's Pizzas", "Organizer Rating": 4.5, "Google Maps Link": "https://maps.app.goo.gl/dJuTHg1BaKFb4zm87"},
        {"Food Option": "Painted Pony", "Organizer Rating": 4.5, "Google Maps Link": "https://maps.app.goo.gl/PLvtoVSDbBmd6cYH8"},
    ]
)


# ABOUT
edited_df = st.data_editor(df)

linktree = 'https://linktr.ee/mtachess'
st.header('About Mount Allison Chess Club')
st.markdown('**MACC All Links** (%s)' % linktree)
st.markdown(
  """
Mount Allison University Chess Club is a student-run organization that aims to provide a platform for students to explore and develop their chess skills. Founded in 2021, the club has grown significantly. Holding 2 unofficial internal and 1 Official CFC Tournament in 2023 with the help of Maritime Chess Club and Dieppe Chess Club. 
""")

# SPONSORS
st.header('Partners & Sponsors')
st.subheader('Maritime Chess Club')

# Create a three-column layout to center the image
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image('mcc_Logo.jpg', use_column_width=True, caption=" ")

# Add the clickable link below the image and center it
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://mcc.devastation.ca/" target="_blank" style="text-decoration: none; color: #B89112;">Visit the Maritime Chess Club</a>
    </div>
    """,
    unsafe_allow_html=True
)
