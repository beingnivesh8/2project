#Essential Libraries

import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import time
import mysql.connector
from sqlalchemy import create_engine

#mycurser and engine created to intreact with MYSQL Database

mydb = mysql.connector.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor(buffered=True,)
engine = create_engine("mysql+mysqlconnector://root:@localhost/phonepe")

#To create and use the database in MYSQL database

mycursor.execute('create database if not exists phonepe')
mycursor.execute('use phonepe')

#Set up page configuration for streamlit

icon='https://cdn.iconscout.com/icon/free/png-512/free-phonepe-2709167-2249157.png?f=webp&w=256'
st.set_page_config(page_title='PHONEPE PULSE',page_icon=icon,initial_sidebar_state='expanded',
                        layout='wide',menu_items={"about":'This streamlit application was developed by Nivesh N P'})

title_text = '''<h1 style='font-size: 36px;color:violet;text-align: center;'>PHONEPE PULSE: The Heartbeat of India's Digital Revolution</h1>'''
st.markdown(title_text, unsafe_allow_html=True)

#Set up home page and optionmenu 

selected = option_menu("Navigation",
                        options=["ABOUT", "HOME", "GEO VISUALIZATION", "INSIGHTS"],
                        icons=["info-circle", "house", "globe", "lightbulb"],
                        default_index=1,
                        orientation="horizontal",
                        styles={"container": {"width": "100%","border": "2px ridge #000000","background-color": "#391C59"},
                                "icon": {"color": "#F8CD47", "font-size": "20px"}})

#Setup the detail for the option 'ABOUT'

if selected == "ABOUT":
        st.subheader(':violet[Project Title:]')
        st.markdown('''<h5>Phonepe Pulse Data Visualization and Exploration:
                        A User-Friendly Tool Using Streamlit and Plotly''',unsafe_allow_html=True)
        st.subheader(':violet[Domain:]')
        st.markdown('<h5>Fintech',unsafe_allow_html=True)
        st.subheader(':violet[Technologies]')
        st.markdown('<h5>Github Cloning, Python, Pandas, MySQL,mysql-connector-python, Streamlit, and Plotly.',unsafe_allow_html=True)
        st.subheader(':violet[Overview:]')
        st.markdown('''
                <h5>Git: Employed Git for version control and efficient collaboration, enabling seamless cloning of the PhonePe dataset from GitHub.<p>
                <h5>Pandas: Leveraged the powerful Pandas library to transform the dataset from JSON format into a structured dataframe.
                Pandas facilitated data manipulation, cleaning, and preprocessing, ensuring the data was ready for analysis.<p>
                <h5>SQL Alchemy: Utilized SQL Alchemy to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                and the data was efficiently inserted into relevant tables for storage and retrieval.<p>
                <h5>Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.<p>
                <h5>Plotly: Integrated Plotly, a versatile plotting library, to generate insightful visualizations from the dataset. Plotly's interactive plots,
                including geospatial plots and other data visualizations, provided users with a comprehensive understanding of the dataset's contents.''',unsafe_allow_html=True)
        st.subheader(':violet[About :]')
        st.markdown('''<h5>Hello! I'm Nivesh N P, a Logistics Junior Engineer with lots of interest in Data science.''',unsafe_allow_html=True)

#Setup the detail for the option 'HOME'

if selected =="HOME":
        col1,col2=st.columns(2)
        with col1:
                st.subheader(':violet[What is Phonepe?]')
                st.markdown('''<h5>PhonePe is a popular digital payments platform in India, offering a range of financial services through its mobile app.
                        Users can make payments, transfer money, recharge phones, pay bills, invest, shop online, and more.<p>
                        <h5>PhonePe has become a preferred choice for millions of users, contributing to India's digital payments revolution.<h5>''',unsafe_allow_html=True)
                
                st.subheader(':violet[what is Phonepe Pulse?]')
                st.markdown('''<h5>PhonePe Pulse provides real-time insights and trends on digital payments across India.
                Its offers comprehensive analytics including transaction volumes, consumer demographics, popular merchant categories,
                geographic trends, transaction values, payment methods, and seasonal fluctuations.<h5>''',unsafe_allow_html=True)
        with col2:
                st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2Vvb2oyaHBqNHZzdm9ycG5lcDEyczk3dDZtcnplamdpbGJudG8xNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gSU4qpRY00OOe6v8I8/giphy-downsized-large.gif)")
        col1,col2=st.columns(2)
        with col1:
                st.image('https://www.phonepe.com/pulsestatic/791/pulse/static/4cb2e7589c30e73dca3d569aea9ca280/1b2a8/pulse-2.webp',use_column_width=True)
        with col2:
                st.write(' ')
                st.subheader(':violet[Discover Insights:]')
                st.markdown('''
                        <h4>Transaction:<h5>Transaction insights involve analyzing customer transaction data to understand behavior and preferences.
                        By examining trends, categorizing transactions,and identifying patterns of india.
                        <h4>User: <h5>User insights refer to analyzing customer demographics, engagement metrics, and feedback.
                        By understanding demographics, tracking engagement of user in India ''',unsafe_allow_html=True)
                
                st.subheader(':violet[This Project is Inspired From Phonepe pulse]')
                st.link_button('Go to Phonepe Pulse','https://www.phonepe.com/pulse/')

        st.subheader(':violet[More About Phonepe Pulse]')
        col1,col2=st.columns(2)
        with col1:
                st.video('https://youtu.be/c_1H6vivsiA?si=lVPODg0axykJgeAZ')
        with col2:
                st.video('https://youtu.be/Yy03rjSUIB8?si=eJRqbCm-K_RDtv0Y')

#Set up details for the option "Geo Visualization"

if selected =="GEO VISUALIZATION":
        
        def ind_geo():
                geo="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                return geo
        
        geo_type = st.radio('Category Selection',["**Transactions**","**Users**"], index = None)
        st.write("You selected:", f"<span style='color:#F8CD47'>{geo_type}</span>", unsafe_allow_html=True)

        if geo_type=="**Transactions**":
                trans_geo_year_wise = st.toggle('Year-Wise')

                if not trans_geo_year_wise:
                        cat=st.radio('Category Selection',["Transaction Amount","Transaction Count"])
                        st.write("You selected:", f"<span style='color:#F8CD47'>{cat}</span>", unsafe_allow_html=True)

                        if cat =="Transaction Amount":
                                st.title(":violet[ Total Transaction Amount for States-Sum of all Year ]")

                                df = pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Total Transaction Amount',
                                        AVG(Transaction_amount) as 'Average Transaction Amount'
                                        from agg_transaction
                                        GROUP by state''',con=engine)
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Amount','Average Transaction Amount'],
                                        color='Total Transaction Amount',
                                        color_continuous_scale='Viridis',
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)

                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.plotly_chart(fig,use_container_width = True)

                        if cat =="Transaction Count":
                                st.title(":violet[Total Transaction Count for States-Sum of all Year]")

                                df = pd.read_sql_query('''SELECT state,sum(Transaction_count) as 'Total Transaction Count',
                                        AVG(Transaction_count) as 'Average Transaction Count'
                                        from agg_transaction
                                        GROUP by state''',con=engine)

                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Count','Average Transaction Count'],
                                        color='Total Transaction Count',
                                        color_continuous_scale='Viridis',
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)

                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.plotly_chart(fig,use_container_width = True)

                if trans_geo_year_wise:
                        df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from agg_transaction''',con=engine)
                        selected_year = st.select_slider("Select Year",options=df_year['Year'].tolist())
                        trans_geo_quater_wise= st.toggle('Quater-Wise')

                        if not trans_geo_quater_wise:
                                df = pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Total Transaction Amount',
                                                AVG(Transaction_amount) as 'Average Transaction Amount',
                                                sum(Transaction_count) as 'Total Transaction Count',
                                                AVG(Transaction_count) as 'Average Transaction Count'
                                                from agg_transaction where year=%s
                                                GROUP by state''',con=engine,params=[(selected_year,)])
                        
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Amount','Average Transaction Amount','Total Transaction Count','Average Transaction Count'],
                                        color='Total Transaction Amount',
                                        color_continuous_scale=px.colors.sequential.Plasma,
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Transaction Amount and Count for States in {selected_year}  ]")
                                st.plotly_chart(fig,use_container_width = True)

                        if trans_geo_quater_wise:
                                df_quater=pd.read_sql_query('''SELECT DISTINCT Quater as 'Quater' from agg_transaction''',con=engine)
                                selected_Quater = st.select_slider("Select Quater",options=df_quater['Quater'].tolist())

                                df = pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Total Transaction Amount',
                                                AVG(Transaction_amount) as 'Average Transaction Amount',
                                                sum(Transaction_count) as 'Total Transaction Count',
                                                AVG(Transaction_count) as 'Average Transaction Count'
                                                from agg_transaction where year=%s and Quater=%s
                                                GROUP by state''',con=engine,params=(selected_year, selected_Quater))
                                
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Amount','Average Transaction Amount','Total Transaction Count','Average Transaction Count'],
                                        color='Total Transaction Amount',
                                        color_continuous_scale=px.colors.sequential.matter_r,
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Transaction Amount and Count for States in {selected_year}-Q{selected_Quater}]")
                                st.plotly_chart(fig,use_container_width = True)
        
        if geo_type=="**Users**":
                user_geo_year_wise = st.toggle('Year-Wise')

                if not user_geo_year_wise:
                        st.title(":violet[ Total Register users Across States-Sum of all Year ]")

                        df = pd.read_sql_query('''SELECT DISTINCT state, SUM(Registered_Users) as 'Total Registered User',
                                        AVG(Registered_Users) as 'Average Register User'
                                        FROM map_user
                                        GROUP BY state''',con=engine)

                        fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Registered User','Average Register User'],
                                        color='Total Registered User',
                                        color_continuous_scale='Viridis',
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)

                        fig.update_geos(fitbounds="locations", visible=False)
                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                        fig.update_layout(height=600)
                        st.plotly_chart(fig,use_container_width = True)

                if user_geo_year_wise:
                        df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from map_user''',con=engine)
                        selected_year = st.select_slider("Select Year",options=df_year['Year'].tolist())
                        user_geo_quater_wise= st.toggle('Quater-Wise')

                        if not user_geo_quater_wise:
                                df = pd.read_sql_query('''SELECT DISTINCT state, SUM(Registered_Users) as 'Total Registered User',
                                                AVG(Registered_Users) as 'Average Register User'
                                                FROM map_user WHERE  year=%s
                                                GROUP BY state''',con=engine,params=[(selected_year,)])
                        
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='state',
                                                hover_data=['Total Registered User','Average Register User'],
                                                color='Total Registered User',
                                                color_continuous_scale=px.colors.sequential.Plasma,
                                                mapbox_style="carto-positron",zoom=3.5,
                                                center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Registered User for States in {selected_year}  ]")
                                st.plotly_chart(fig,use_container_width = True)

                        if user_geo_quater_wise:
                                df_quater=pd.read_sql_query('''SELECT DISTINCT Quater as 'Quater' from map_user''',con=engine)
                                selected_Quater = st.select_slider("Select Quater",options=df_quater['Quater'].tolist())

                                df = pd.read_sql_query('''SELECT DISTINCT state, SUM(Registered_Users) as 'Total Registered User',
                                                AVG(Registered_Users) as 'Average Register User'
                                                FROM map_user WHERE  year=%s and Quater=%s
                                                GROUP BY state''',con=engine,params=(selected_year,selected_Quater))
                        
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='state',
                                                hover_data=['Total Registered User','Average Register User'],
                                                color='Total Registered User',
                                                color_continuous_scale=px.colors.sequential.matter_r,
                                                mapbox_style="carto-positron",zoom=3.5,
                                                center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Registered User for States in {selected_year}-Q{selected_Quater} ]")
                                st.plotly_chart(fig,use_container_width = True)

#Setup details for the option 'Insights'

if selected =="INSIGHTS":
        select_insight=option_menu('',options=["TOP INSIGHTS","FILTER INSIGHTS"],
                                icons=["bar-chart", "toggles"],
                                orientation='horizontal',
                                styles={"container":{"border": "2px ridge #000000"},
                                "icon": {"color": "#F8CD47", "font-size": "20px"}})
        if select_insight =="TOP INSIGHTS":
                qust=[  'Top 10 states with highest transaction',
                        'Top 10 states with lowest transaction',
                        'Top 10 states with highest Registered User',
                        'Top 10 District with highest transaction',
                        'Top 10 District with lowest transaction',
                        'Top 10 District with highest Registered User',
                        'Top 10 Brands used for Transaction',
                        'Sum of Transaction by Type or categories',
                        'Top 10 Postal code with highest Transaction',
                        'Top 10 Postal code with highest Registered user'
                        ]
                query=st.selectbox(':red[Select a Query]',options=qust,index=None)

                #for write stream created a function
                def stream1():
                                for i in t_1:
                                        yield i + ''
                                        time.sleep(0.02)
                def stream2():
                                for i in t_2:
                                        yield i + ''
                                        time.sleep(0.02)
                def stream3():
                                for i in t_3:
                                        yield i + ''
                                        time.sleep(0.02)
                def stream4():
                                for i in t_4:
                                        yield i + ''
                                        time.sleep(0.02)

                if query=='Top 10 states with highest transaction':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Transaction Amount'
                                        from agg_transaction
                                        GROUP by state
                                        ORDER by sum(Transaction_amount) DESC LIMIT 10;''',con=engine)
                                
                                fig=px.bar(df,x='state',y='Transaction Amount',
                                                color='state',
                                                hover_data=['Transaction Amount'],
                                                title='Top 10 state of Highest Transaction Amount',
                                                color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        with col2:
                                df=pd.read_sql_query('''SELECT state, SUM(Transaction_count) AS 'Transaction Count' FROM agg_transaction
                                                WHERE state IN ( SELECT state FROM 
                                                (SELECT state, SUM(Transaction_amount) AS amount FROM agg_transaction 
                                                GROUP BY state ORDER BY amount DESC LIMIT 10 )as top_state )
                                                GROUP BY state order by sum(Transaction_count) DESC''',con=engine)
                                
                                fig=px.bar(df,x='state',y='Transaction Count',
                                                color='Transaction Count',
                                                hover_data=['Transaction Count'],
                                                title='Transaction Count',
                                                color_continuous_scale=px.colors.carto.Emrld_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        t_1=('''🟡Telangana has seen significant growth in technology and IT-related industries, especially in cities like Hyderabad.
                        This growth has likely led to increased digital transactions through phonepe.''')
                        
                        t_2=('''🟡Maharashtra is home to Mumbai, the financial capital of India, and has a diverse economy spanning finance, manufacturing, and services.
                        High urbanization and economic activity contribute to its high transaction amounts.''')
                        
                        t_3=('''🟡Karnataka particularly Bengaluru, is another major hub for technology and innovation. 
                        The presence of numerous IT companies and startups likely drives a large volume of digital transactions.''')
                        
                        t_4=('''🟡States like Andhra Pradesh, Rajasthan, Uttar Pradesh, Madhya Pradesh, Bihar, West Bengal and
                        Tamil Nadu have all shown significant growth in digital transactions. 
                        This growth is fueled by initiatives promoting digital adoption, increasing urbanization rates,
                        efforts to improve financial inclusion and digital literacy,
                        and the presence of diverse economic sectors driving the shift towards digital payments''')

                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Top 10 states with lowest transaction':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Transaction Amount'
                                        from agg_transaction GROUP by state
                                        ORDER by sum(Transaction_amount) ASC LIMIT 10''',con=engine)
                                df['state']=df['state'].str.replace('Dadra and Nagar Haveli and Daman and Diu','Dadra')

                                fig=px.bar(df,x='state',y='Transaction Amount',
                                                color='state',
                                                hover_data=['Transaction Amount'],
                                                title='Top 10 state of lowest Transaction Amount',
                                                color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)
                        
                        with col2:
                                df=pd.read_sql_query('''SELECT state, SUM(Transaction_count) AS 'Transaction Count' FROM agg_transaction
                                                WHERE state IN ( SELECT state FROM 
                                                (SELECT state, SUM(Transaction_amount) AS amount FROM agg_transaction 
                                                GROUP BY state ORDER BY amount ASC LIMIT 10 )as top_state )
                                                GROUP BY state order by sum(Transaction_count) ASC''',con=engine)
                                df['state']=df['state'].str.replace('Dadra and Nagar Haveli and Daman and Diu','Dadra')
                                
                                fig=px.bar(df,x='state',y='Transaction Count',
                                                color='Transaction Count',
                                                hover_data=['Transaction Count'],
                                                title='Transaction Count',
                                                color_continuous_scale=px.colors.carto.Emrld_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        t_1='''🟡 Lakshadweep has Limited population and remote island location result in restricted access to digital 
                        infrastructure and financial services'''
                        t_2='''🟡 Mizoram: Sparse population and hilly terrain pose challenges in digital infrastructure and connectivity.
                        Limited economic diversification and lower urbanization rates may also contribute to lower transaction volumes'''
                        t_3='''🟡 Andaman & Nicobar Islands: Geographical constraints and a relatively small population limit access to digital services.
                        Although the tourism industry is significant, seasonal fluctuations and reliance on cash payments may hinder digital transaction growth.'''
                        t_4='''🟡 For the remaining states, including Ladakh, Sikkim, Nagaland, Meghalaya, Dadra & Nagar Haveli, Tripura, and Manipur, a
                        combination of factors contributes to lower transaction amounts. These states often face challenges such as rugged terrain, 
                        scattered population, limited economic diversification, and cultural preferences for cash transactions.'''

                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Top 10 states with highest Registered User':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT state ,sum(Registered_Users) as 'Registered User' FROM map_user 
                                                GROUP BY state ORDER BY sum(Registered_Users) DESC limit 10''',con=engine)
                                
                                fig=px.bar(df,x='state',y='Registered User',
                                                color='state',
                                                hover_data=['Registered User'],
                                                title='Top 10 state of highest Registered User',
                                                color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        with col2:
                                df=pd.read_sql_query('''SELECT state, SUM(App_Opens) AS 'App Opened' FROM map_user WHERE state IN 
                                                (SELECT state  FROM (SELECT state, SUM(Registered_Users) AS 'R_user'
                                                FROM map_user GROUP BY state ORDER BY sum(Registered_Users) DESC LIMIT 10)as top_user )
                                                GROUP BY state ORDER BY sum(App_Opens) DESC''',con=engine)
                                
                                fig=px.bar(df,x='state',y='App Opened',
                                                color='App Opened',
                                                hover_data=['App Opened'],
                                                title='App Opened',
                                                color_continuous_scale=px.colors.carto.Emrld_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)
                        
                        t_1='''🟡 Maharashtra tops the list with the highest number of PhonePe registered users, indicating a strong adoption 
                        of digital payment platforms in the state's urban and rural areas.'''
                        t_2='''🟡 Uttar Pradesh, Karnataka, and Andhra Pradesh closely follow, showcasing substantial PhonePe user registrations
                        and widespread acceptance of digital transactions in these populous states.'''
                        t_3='''🟡 Rajasthan, Telangana, and West Bengal demonstrate notable PhonePe user bases, 
                        reflecting increasing digital adoption in regional economic centers and urban clusters.'''
                        t_4='''🟡 Tamil Nadu, Madhya Pradesh, and Gujarat contribute significantly to the overall PhonePe user base, 
                        highlighting the diverse digital landscapes and growing popularity of digital payment solutions across different regions of India.'''

                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Top 10 District with highest transaction':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT District,sum(Transaction_amount) as 'Transaction Amount'
                                        from map_transaction GROUP by District
                                        ORDER by sum(Transaction_amount) DESC LIMIT 10;''',con=engine)
                                df['District']=df['District'].str.replace('Central','Delhi Central')
                                
                                fig=px.bar(df,x='District',y='Transaction Amount',
                                                color='District',
                                                hover_data=['Transaction Amount'],
                                                title='Top 10 District of Highest Transaction Amount',
                                                color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        with col2:
                                df=pd.read_sql_query('''SELECT District, SUM(Transaction_count) AS 'Transaction Count' FROM map_transaction 
                                        WHERE District IN (SELECT District  FROM (SELECT District, SUM(Transaction_amount) AS 'amount' 
                                        FROM map_transaction GROUP BY District ORDER BY amount DESC LIMIT 10)as top_dist )
                                        GROUP BY District ORDER BY SUM(Transaction_count) DESC;''',con=engine)
                                df['District']=df['District'].str.replace('Central','Delhi Central')

                                fig=px.bar(df,x='District',y='Transaction Count',
                                                color='Transaction Count',
                                                hover_data=['Transaction Count'],
                                                title='Transaction Count',
                                                color_continuous_scale=px.colors.carto.Emrld_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)
                        
                        t_1='''🟡 Bengaluru, Hyderabad, and Pune stand out as primary centers for PhonePe transactions, 
                        driven by their prominence in the IT and business sectors and widespread smartphone usage.'''
                        t_2='''🟡 Jaipur and Visakhapatnam spearhead PhonePe transactions within their regions, 
                        benefitting from a mix of traditional commerce and burgeoning tech industries.'''
                        t_3='''🟡 Rangareddy and Medchal Malkajgiri, integral to Hyderabad's metropolitan area, exhibit noteworthy PhonePe
                        transaction volumes,showcasing the increasing acceptance of digital payments in urban environments.'''
                        t_4='''🟡 Patna, Krishna, and Delhi Central demonstrate substantial PhonePe transactions, driven by their administrative 
                        significance, strategic positioning, and bustling commercial landscapes, indicating a widespread embrace of digital payment platforms.'''
                        
                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Top 10 District with lowest transaction':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT District,sum(Transaction_amount) as 'Transaction Amount'
                                        from map_transaction GROUP by District
                                        ORDER by sum(Transaction_amount) ASC LIMIT 10;''',con=engine)
                                
                                fig=px.bar(df,x='District',y='Transaction Amount',
                                                color='District',
                                                hover_data=['Transaction Amount'],
                                                title='Top 10 District of Lowest Transaction Amount',
                                                color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)
                        with col2:
                                df=pd.read_sql_query('''SELECT District, SUM(Transaction_count) AS 'Transaction Count' FROM map_transaction 
                                        WHERE District IN (SELECT District  FROM (SELECT District, SUM(Transaction_amount) AS 'amount' 
                                        FROM map_transaction GROUP BY District ORDER BY amount ASC LIMIT 10)as top_dist )
                                        GROUP BY District ORDER BY SUM(Transaction_count) ASC;''',con=engine)

                                fig=px.bar(df,x='District',y='Transaction Count',
                                                color='Transaction Count',
                                                hover_data=['Transaction Count'],
                                                title='Transaction Count',
                                                color_continuous_scale=px.colors.carto.Emrld_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        t_1='''🟡 Districts like Pherzawl and Dibang Valley, with their rural settings, 
                        witness fewer transactions due to limited digital infrastructure and financial services.'''
                        t_2='''🟡 Areas like Pakke Kessang and Kurung Kumey may have lower transaction amounts due to sparse 
                        population densities, resulting in fewer digital transactions compared to more densely populated regions.'''
                        t_3='''🟡 Districts like Muzaffarabad and Longleng face infrastructure hurdles like poor internet connectivity,
                        hindering digital payment adoption.'''
                        t_4='''🟡 Socioeconomic factors and cultural preferences for cash transactions also contribute to 
                        lower digital payment adoption in these regions.'''

                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Top 10 Brands used for Transaction':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT DISTINCT User_brand as 'User Brand' ,SUM(User_count) as 'Count'
                                                FROM agg_user GROUP BY User_brand
                                                order by SUM(User_count) DESC LIMIT 10''',con=engine)
                                
                                fig=px.bar(df,x='User Brand',y='Count',
                                                color='User Brand',
                                                hover_data=['Count'],
                                                title='Top 10 Brands used for Transaction (sum of all states)',
                                                color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        with col2:
                                df=pd.read_sql_query('''SELECT User_brand AS 'User Brand', (SUM(User_count) / total_count) * 100 AS 'Percentage'
                                                FROM agg_user
                                                CROSS JOIN (SELECT SUM(User_count) AS total_count FROM agg_user) AS total
                                                GROUP BY User_brand
                                                ORDER BY SUM(User_count) DESC LIMIT 10;''',con=engine)
                                
                                fig=px.pie(df,names='User Brand',values='Percentage',color='User Brand',
                                                title='Percentage',
                                                color_discrete_sequence=px.colors.qualitative.Bold)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)
                        
                        t_1='''🟡 Xiaomi, Samsung, Vivo, and Oppo dominate transactions due to their wide range of products and strong brand recognition. 
                        and thier affordability,innovation,focus on camera technology and stylish designs collectively drive consumer purchases.'''
                        t_2='''🟡 Realme, Motorola, and OnePlus gain market share with competitive pricing and innovative features. Realme's rapid growth,
                        Motorola's reliability, and OnePlus's flagship-level features appeal to budget-conscious and tech-savvy consumers.'''
                        t_3='''🟡 Apple and Huawei maintain transaction volumes through premium branding and advanced technology.
                        and thier aspirational value and loyal customer base, along with reputation for innovation, drive transactions in the premium smartphone segment.'''
                        t_4='''🟡 Other brands cater to niche segments, offering budget-friendly options and diversifying the market.
                        These brands contribute to overall transaction volumes by providing alternative choices for consumers'''
                        
                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Top 10 District with highest Registered User':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT District, sum(Registered_Users) as 'Registered User' FROM map_user
                                        GROUP BY District ORDER BY sum(Registered_Users) DESC LIMIT 10''',con=engine)
                                
                                fig=px.bar(df,x='District',y='Registered User',
                                                color='District',
                                                hover_data=['Registered User'],
                                                title='Top 10 District of highest Registered User ',
                                                color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        with col2:
                                df=pd.read_sql_query('''SELECT District, SUM(App_Opens) AS 'App Opened' FROM map_user WHERE District IN 
                                                (SELECT District  FROM (SELECT District, SUM(Registered_Users) AS 'R_user'
                                                FROM map_user GROUP BY District ORDER BY sum(Registered_Users) DESC LIMIT 10)as top_user )
                                                GROUP BY District ORDER BY sum(App_Opens) DESC''',con=engine)
                                
                                fig=px.bar(df,x='District',y='App Opened',
                                                color='App Opened',
                                                hover_data=['App Opened'],
                                                title='App Opened',
                                                color_continuous_scale=px.colors.carto.Emrld_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        t_1='''🟡 Bengaluru Urban emerges as the district with the highest number of registered PhonePe users, 
                        indicating a strong adoption of digital payment platforms in Karnataka's capital city and its surrounding urban areas.'''
                        t_2='''🟡 Pune and Jaipur secure the second and third positions, respectively, in terms of PhonePe registrations,
                        showcasing significant digital adoption in Maharashtra and Rajasthan's urban centers.'''
                        t_3='''🟡 Districts like Thane, Mumbai Suburban, and Hyderabad demonstrate substantial PhonePe user bases, 
                        reflecting a strong urban presence and a growing preference for digital payment solutions in metropolitan areas.'''
                        t_4='''🟡 Districts like Ahmedabad, Rangareddy, and Surat represent diverse regions and contribute notably to PhonePe registrations,
                        reflecting a broader adoption trend beyond metropolitan areas'''
                        
                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Sum of Transaction by Type or categories':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT DISTINCT Transaction_type as 'categories',SUM(Transaction_amount) as 'Transaction Amount'
                                                        from agg_transaction GROUP BY Transaction_type DESC''',con=engine)
                                
                                fig=px.pie(df,names='categories',values='Transaction Amount',color='categories',
                                                title='Sum of Transaction Amount by categories',hole=0.3,
                                                color_discrete_sequence=px.colors.qualitative.Bold)
                                st.plotly_chart(fig,use_container_width=True)
                        
                        with col2:
                                st.subheader('Sum of Transaction Amount')
                                st.dataframe(df,hide_index=True)
                        
                        t_1='''🟡 Peer-to-peer payments stand out as the largest category, with an overwhelming transaction amount of 169.78 trillion.
                        This suggests a significant volume of person-to-person financial transactions within the observed period.'''
                        t_2='''🟡 Merchant payments (37.36 trillion)and recharge/bill payments (8.53 trillion) signify
                        substantial commercial and essential service transactions.'''
                        t_3='''🟡 Financial services transactions, though smaller at 80.10 billion,
                        highlight the importance of banking and investment activities.'''
                        t_4='''🟡 The 141.85 billion in "Others" suggests diverse financial activities beyond specified categories.'''

                        st.write_stream(stream1())
                        st.write_stream(stream2())
                        st.write_stream(stream3())
                        st.write_stream(stream4())

                if query=='Top 10 Postal code with highest Transaction':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT Pincode, sum(Transaction_amount) as 'Transaction Amount' FROM top_transaction
                                                GROUP BY Pincode ORDER BY sum(Transaction_amount) DESC LIMIT 10''',con=engine)
                                
                                fig=px.pie(df,names='Pincode',values='Transaction Amount',
                                                color="Pincode",
                                                title='Top 10 Postal code of highest Transaction Amount ',
                                                color_discrete_sequence=px.colors.qualitative.Pastel_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                        with col2:
                                df=pd.read_sql_query('''SELECT Pincode , SUM(Transaction_count) AS 'Transaction Count' FROM top_transaction
                                                WHERE Pincode IN (SELECT Pincode FROM (SELECT Pincode, SUM(Transaction_amount) AS 't_amt' 
                                                FROM top_transaction GROUP BY Pincode ORDER BY SUM(Transaction_amount) DESC LIMIT 10)as top_tran ) 
                                                GROUP BY Pincode ORDER BY SUM(Transaction_count) DESC;''',con=engine)
                                
                                fig=px.pie(df,names='Pincode',values='Transaction Count',
                                                color='Transaction Count',
                                                title='Transaction Count',
                                                color_discrete_sequence=px.colors.qualitative.Dark2_r)
                                st.plotly_chart(fig,use_container_width=True)
                                st.dataframe(df,hide_index=True)

                if query=='Top 10 Postal code with highest Registered user':
                        col1,col2=st.columns(2)
                        with col1:
                                df=pd.read_sql_query('''SELECT Pincode, sum(Registered_Users) as 'Registered user' FROM top_user
                                                GROUP BY Pincode ORDER BY  sum(Registered_Users) DESC LIMIT 10''',con=engine)
                                
                                fig=px.pie(df,names='Pincode',values='Registered user',
                                                color="Pincode",
                                                title='Top 10 Postal code with highest Registered user ',
                                                color_discrete_sequence=px.colors.qualitative.Pastel_r)
                                st.plotly_chart(fig,use_container_width=True)

                        with col2:
                                st.write('Top 10 Postal code with highest Registered user')
                                st.dataframe(df,hide_index=True)

        if select_insight =="FILTER INSIGHTS":
                fil_type=st.radio('Category Selection',["**State**","**District**"], index = None)
                st.write("You selected:", f"<span style='color:#F8CD47'>{fil_type}</span>", unsafe_allow_html=True)

                if fil_type=="**State**":
                        ques=['Year and Quater wise Transaction Amount of all states',
                                'Quater wise Transaction Amount for specific state',
                                'Transaction Category with specific state and year',
                                'Quater wise Transaction Amount for specific state and type',
                                'User Brand Count for selected state and year',
                                'Quater wise Registered User Count for selected state and year']
                        Query=st.selectbox(':red[select Query]',options=ques,index=None)

                        if Query==ques[0]:
                                df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from agg_transaction''',con=engine)
                                select_year = st.selectbox("Select Year",options=df_year['Year'].tolist(),index=None)

                                df_quater=pd.read_sql_query('''SELECT DISTINCT Quater as 'Quater' from agg_transaction''',con=engine)
                                select_Quater = st.selectbox("Select Quater",options=df_quater['Quater'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        df=pd.read_sql_query('''SELECT state, SUM(Transaction_amount) as 'Transaction Amount'
                                        FROM agg_transaction where year = %s and Quater = %s
                                        GROUP BY state''',con=engine,params=[(select_year,select_Quater)])

                                        fig=px.scatter(df,x='state',y='Transaction Amount',
                                                        title=f'Showing Transaction Amount of {select_year}-Q{select_Quater}')
                                        st.plotly_chart(fig,use_container_width=True)

                                        df1=pd.read_sql_query('''SELECT state, SUM(Transaction_count) as 'Transaction Count'
                                        FROM agg_transaction where year = %s and Quater = %s
                                        GROUP BY state''',con=engine,params=[(select_year,select_Quater)])

                                        fig=px.scatter(df1,x='state',y='Transaction Count',
                                                        title=f'Showing Transaction Count of {select_year}-Q{select_Quater}')
                                        st.plotly_chart(fig,use_container_width=True)

                                        col1,col2=st.columns(2)
                                        with col1:
                                                st.dataframe(df,hide_index=True)
                                        with col2:
                                                st.dataframe(df1,hide_index=True)
                        
                        if Query==ques[1]:
                                df_state=pd.read_sql_query('''Select DISTINCT state from agg_transaction''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from agg_transaction''',con=engine)
                                select_year = st.selectbox("Select Year",options=df_year['Year'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        col1,col2=st.columns(2)
                                        with col1:
                                                df=pd.read_sql_query(''' SELECT Quater,sum(Transaction_amount) as 'Transaction Amount'
                                                                from agg_transaction WHERE state=%s and year=%s
                                                                GROUP by Quater;''',con=engine,params=[(select_state,select_year)])
                                                
                                                fig=px.bar(df,x='Quater',y='Transaction Amount',
                                                        color='Transaction Amount',hover_data=['Transaction Amount'],
                                                        title=f'Quater wise Transaction Amount of {select_state} for the year:{select_year}',
                                                        color_continuous_scale=px.colors.carto.Emrld_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)
                                        
                                        with col2:
                                                df=pd.read_sql_query(''' SELECT Quater,sum(Transaction_count) as 'Transaction Count'
                                                                from agg_transaction WHERE state=%s and year=%s
                                                                GROUP by Quater;''',con=engine,params=[(select_state,select_year)])
                                                
                                                fig=px.bar(df,x='Quater',y='Transaction Count',
                                                        color='Transaction Count',hover_data=['Transaction Count'],
                                                        title=f'Quater wise Transaction Count of {select_state} for the year: {select_year}',
                                                        color_continuous_scale=px.colors.carto.Blugrn_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                        if Query==ques[2]:
                                df_state=pd.read_sql_query('''Select DISTINCT state from agg_transaction''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from agg_transaction''',con=engine)
                                select_year = st.selectbox("Select Year",options=df_year['Year'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        col1,col2=st.columns(2)
                                        with col1:
                                                df=pd.read_sql_query(''' SELECT Transaction_type as 'category',sum(Transaction_amount) as 'Transaction Amount'
                                                                from agg_transaction WHERE state=%s and year=%s
                                                                GROUP BY Transaction_type''',con=engine,params=[(select_state,select_year)])
                                                
                                                fig=px.bar(df,x='category',y='Transaction Amount',
                                                        color='Transaction Amount',hover_data=['Transaction Amount'],
                                                        title=f'Categories of Transaction Amount of {select_state} for the year:{select_year}',
                                                        color_continuous_scale=px.colors.carto.Emrld_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                                        with col2:
                                                df=pd.read_sql_query(''' SELECT Transaction_type as 'category',sum(Transaction_count) as 'Transaction Count'
                                                                from agg_transaction WHERE state=%s and year=%s
                                                                GROUP BY Transaction_type''',con=engine,params=[(select_state,select_year)])
                                                
                                                fig=px.bar(df,x='category',y='Transaction Count',
                                                        color='Transaction Count',hover_data=['Transaction Count'],
                                                        title=f'Categories of Transaction Count of {select_state} for the year:{select_year}',
                                                        color_continuous_scale=px.colors.carto.Emrld_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                        if Query==ques[3]:
                                df_state=pd.read_sql_query('''Select DISTINCT state from agg_transaction''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_type=pd.read_sql_query('''SELECT DISTINCT Transaction_type as 'Type' from agg_transaction''',con=engine)
                                select_type=st.selectbox('Select Type',options=df_type['Type'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        col1,col2=st.columns(2)
                                        with col1:
                                                df=pd.read_sql_query('''SELECT state,Quater,sum(Transaction_amount) as 'Transaction Amount' from agg_transaction 
                                                                where state =%s and Transaction_type=%s group by state,Quater''',con=engine,params=[(select_state,select_type)])
                                                
                                                fig=px.bar(df,x='Quater',y='Transaction Amount',
                                                                        color='Transaction Amount',hover_data=['Transaction Amount'],
                                                                        title=f'showing quater wise Amount of {select_state} for type:{select_type}',
                                                                        color_continuous_scale=px.colors.carto.Emrld_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                                        with col2:
                                                df=pd.read_sql_query('''SELECT state,Quater,sum(Transaction_count) as 'Transaction Count' from agg_transaction 
                                                                where state =%s and Transaction_type=%s group by state,Quater''',con=engine,params=[(select_state,select_type)])
                                                
                                                fig=px.bar(df,x='Quater',y='Transaction Count',
                                                                        color='Transaction Count',hover_data=['Transaction Count'],
                                                                        title=f'showing quater wise Count of {select_state} for type:{select_type}',
                                                                        color_continuous_scale=px.colors.carto.Emrld_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                        if Query==ques[4]:
                                df_state=pd.read_sql_query('''Select DISTINCT state from agg_user''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from agg_user''',con=engine)
                                select_year = st.selectbox("Select Year",options=df_year['Year'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        col1,col2=st.columns(2)
                                        with col1:
                                                df=pd.read_sql_query('''SELECT User_brand as 'User Brand',sum(User_count) as 'Count' from agg_user
                                                        WHERE state=%s and year=%s
                                                        GROUP by User_brand order by sum(User_count) DESC''',con=engine,params=[(select_state,select_year)])
                                                
                                                fig=px.bar(df,x='User Brand',y='Count',
                                                        color='Count',hover_data=['Count'],
                                                        title=f'Showing User Brand Count of {select_state} for the year:{select_year}',
                                                        color_continuous_scale=px.colors.carto.Emrld_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                                        with col2:
                                                fig=px.pie(df,names='User Brand',values='Count',
                                                        color='User Brand',title='Count Percentage',
                                                        color_discrete_sequence=px.colors.qualitative.Bold_r)
                                                st.plotly_chart(fig,use_container_width=True)

                        if Query==ques[5]:
                                df_state=pd.read_sql_query('''Select DISTINCT state from map_user''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from map_user''',con=engine)
                                select_year = st.selectbox("Select Year",options=df_year['Year'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        col1,col2=st.columns(2)
                                        with col1:
                                                df=pd.read_sql_query('''SELECT Quater,sum(Registered_Users) as 'Registered Users' from map_user
                                                                WHERE state =%s and year=%s
                                                                GROUP by Quater''',con=engine,params=[(select_state,select_year)])
                                                
                                                fig=px.bar(df,x='Quater',y='Registered Users',
                                                        color='Registered Users',hover_data=['Registered Users'],
                                                        title=f'Showing Registered Users Count of {select_state} for the year:{select_year}',
                                                        color_continuous_scale=px.colors.carto.Emrld_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)
                                        
                                        with col2:
                                                df=pd.read_sql_query('''SELECT Quater,sum(App_Opens) as 'App opened' from map_user
                                                                WHERE state =%s and year=%s
                                                                GROUP by Quater''',con=engine,params=[(select_state,select_year)])
                                                
                                                fig=px.pie(df,names='Quater',values='App opened',
                                                        color='App opened',title='App opened',
                                                        color_discrete_sequence=px.colors.qualitative.Bold_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                if fil_type=="**District**":
                        ques=['District wise Transaction Amount for selected state & year',
                                'Year wise Transaction Amount for specific District',
                                'Year wise Registered User Count for Specific District']
                        Query=st.selectbox(':red[select Query]',options=ques,index=None)

                        if Query==ques[0]:
                                df_state=pd.read_sql_query('''SELECT DISTINCT state from map_transaction''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_year=pd.read_sql_query('''SELECT DISTINCT year from map_transaction''',con=engine)
                                select_year = st.selectbox("Select Year",options=df_year['year'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        df=pd.read_sql_query('''SELECT District, SUM(Transaction_amount) as 'Transaction Amount'
                                        FROM map_transaction where state=%s and  year =%s
                                        GROUP BY District''',con=engine,params=[(select_state,select_year)])

                                        fig=px.bar(df,x='District',y='Transaction Amount',
                                                        color='Transaction Amount',hover_data=['Transaction Amount'],
                                                        title=f'District wise Transaction Amount of {select_state} for the year:{select_year}',
                                                        color_continuous_scale=px.colors.colorbrewer.Blues_r)
                                        st.plotly_chart(fig,use_container_width=True)

                                        df1=pd.read_sql_query('''SELECT District, SUM(Transaction_count) as 'Transaction count'
                                        FROM map_transaction where state=%s and  year =%s
                                        GROUP BY District''',con=engine,params=[(select_state,select_year)])

                                        fig=px.bar(df1,x='District',y='Transaction count',
                                                        color='Transaction count',hover_data=['Transaction count'],
                                                        title=f'District wise Transaction count of {select_state} for the year:{select_year}',
                                                        color_continuous_scale=px.colors.colorbrewer.Blues_r)
                                        st.plotly_chart(fig,use_container_width=True)

                                        col1,col2=st.columns(2)
                                        with col1:
                                                st.dataframe(df,hide_index=True)
                                        with col2:
                                                st.dataframe(df1,hide_index=True)
                        
                        if Query==ques[1]:
                                df_state=pd.read_sql_query('''SELECT DISTINCT state from map_transaction''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_dist=pd.read_sql_query('''SELECT DISTINCT District FROM map_transaction 
                                                        where state=%s''',con=engine,params=[(select_state,)])
                                select_dist=st.selectbox('Select District',options=df_dist['District'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        col1,col2=st.columns(2)
                                        with col1:
                                                df=pd.read_sql_query('''SELECT year,sum(Transaction_amount) as 'Transaction Amount' from map_transaction
                                                        where state=%s and District= %s
                                                        GROUP by year''',con=engine,params=[(select_state,select_dist)])
                                                
                                                fig=px.bar(df,x='year',y='Transaction Amount',
                                                        color='Transaction Amount',hover_data=['Transaction Amount'],
                                                        title=f'Year wise Transaction Amount of {select_dist} District',
                                                        color_continuous_scale=px.colors.colorbrewer.Blues_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                                        with col2:
                                                df=pd.read_sql_query('''SELECT year,sum(Transaction_count) as 'Transaction count' from map_transaction
                                                        where state=%s and District= %s
                                                        GROUP by year''',con=engine,params=[(select_state,select_dist)])
                                                
                                                fig=px.bar(df,x='year',y='Transaction count',
                                                        color='Transaction count',hover_data=['Transaction count'],
                                                        title=f'Year wise Transaction count of {select_dist} District',
                                                        color_continuous_scale=px.colors.colorbrewer.Blues_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                        if Query==ques[2]:
                                df_state=pd.read_sql_query('''SELECT DISTINCT state from map_transaction''',con=engine)
                                select_state=st.selectbox('Select state',options=df_state['state'].tolist(),index=None)

                                df_dist=pd.read_sql_query('''SELECT DISTINCT District FROM map_transaction 
                                                        where state=%s''',con=engine,params=[(select_state,)])
                                select_dist=st.selectbox('Select District',options=df_dist['District'].tolist(),index=None)
                                bt=st.button('Show')
                                if bt:
                                        col1,col2=st.columns(2)
                                        with col1:
                                                df=pd.read_sql_query('''SELECT year,sum(Registered_Users) as 'Registered User' from map_user
                                                        where state=%s and District= %s
                                                        GROUP by year''',con=engine,params=[(select_state,select_dist)])
                                                
                                                fig=px.bar(df,x='year',y='Registered User',
                                                        color='Registered User',hover_data=['Registered User'],
                                                        title=f'Year wise Registered User of {select_dist} District',
                                                        color_continuous_scale=px.colors.colorbrewer.Blues_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)

                                        with col2:
                                                df=pd.read_sql_query('''SELECT year,sum(App_Opens) as 'App opened' from map_user
                                                        where state=%s and District= %s
                                                        GROUP by year''',con=engine,params=[(select_state,select_dist)])
                                                
                                                fig=px.pie(df,names='year',values='App opened',
                                                        color='App opened',title='App opened',
                                                        color_discrete_sequence=px.colors.qualitative.Bold_r)
                                                st.plotly_chart(fig,use_container_width=True)
                                                st.dataframe(df,hide_index=True)
