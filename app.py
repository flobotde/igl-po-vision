import streamlit as st                                                                                                                
import numpy as np                                                                                                                    
import pandas as pd                                                                                                                   
import plotly.express as px                                                                                                           
import time                                                                                                                           
# Set the title of the dashboard
st.title("IGL PO Vision Dashboard")                                                                                                   

# Function to simulate dynamic data                                                                                                   
def simulate_dynamic_data():                                                                                                          
    # Simulate data for each metric                                                                                                   
    data = {                                                                                                                          
            "Gesamtverfügbarkeit": np.random.uniform(99.5, 100),                                                                          
            "Aktive Integrationsstrecken": np.random.randint(10, 20),                                                                     
            "CPU-Auslastung": np.random.uniform(30, 70),                                                                                  
            "Speicherauslastung": np.random.uniform(40, 80),                                                                              
            "Netzwerkauslastung": np.random.uniform(20, 60),                                                                              
            "Durchschnittliche Verarbeitungszeit": np.random.uniform(150, 250),                                                           
            "Datendurchsatz": np.random.uniform(400, 600),                                                                                
            "Fehlerrate": np.random.uniform(0, 0.5),                                                                                      
            "Prozentsatz korrekter Datensätze": np.random.uniform(95, 100),                                                               
            "Durchschnittliche Verzögerung": np.random.uniform(80, 120),                                                                  
            "Fehlgeschlagene Authentifizierungsversuche": np.random.randint(0, 5),                                                        
            "Erfüllung von SLAs": np.random.uniform(99, 100)                                                                              
            }                                                                                                                                 
    return data                                                                                                                       

# Create a placeholder for the charts                                                                                                 
placeholder = st.empty()                                                                                                              
# Simulate and update the data every few seconds                                                                                      
while True:                                                                                                                           
    data = simulate_dynamic_data()
    with placeholder.container():                                                                                                     
        # System Health                                                                                                               
        st.subheader("Systemgesundheit")                                                                                              
        st.metric("Gesamtverfügbarkeit", f"{data['Gesamtverfügbarkeit']:.2f}%")                                                       
        st.metric("Aktive Integrationsstrecken", data['Aktive Integrationsstrecken'])                                                 
        # Resource Utilization                                                                                                        
        st.subheader("Ressourcenauslastung")                                                                                          
        fig = px.bar(x=["CPU", "Speicher", "Netzwerk"], y=[data['CPU-Auslastung'], data['Speicherauslastung'],data['Netzwerkauslastung']], labels={'x': 'Ressource', 'y': 'Auslastung (%)'})                                                        
        st.plotly_chart(fig)                                                                                                          

        # Performance Metrics                                                                                                         
        st.subheader("Leistungsmetriken")                                                                                             
        st.metric("Durchschnittliche Verarbeitungszeit", f"{data['Durchschnittliche Verarbeitungszeit']:.2f} ms")                     
        st.metric("Datendurchsatz", f"{data['Datendurchsatz']:.2f} MB/s")                                                             
        # Error Metrics                                                                                                               
        st.subheader("Fehlermetriken")                                                                                                
        st.metric("Fehlerrate", f"{data['Fehlerrate']:.2f}%")                                                                         
        # Data Quality                                                                                                                
        st.subheader("Datenqualität")                                                                                                 
        st.metric("Prozentsatz korrekter Datensätze", f"{data['Prozentsatz korrekter Datensätze']:.2f}%")                             
        # Latency                                                                                                                     
        st.subheader("Latenzzeiten")                                                                                                  
        st.metric("Durchschnittliche Verzögerung", f"{data['Durchschnittliche Verzögerung']:.2f} ms")                                 
        # Security Metrics                                                                                                            
        st.subheader("Sicherheitsmetriken")                                                                                           
        st.metric("Fehlgeschlagene Authentifizierungsversuche", data['Fehlgeschlagene Authentifizierungsversuche'])                   
        # Business KPIs                                                                                                               
        st.subheader("Geschäftliche KPIs")                                                                                            
        st.metric("Erfüllung von SLAs", f"{data['Erfüllung von SLAs']:.2f}%")                                                         
    # Wait for a few seconds before updating                                                                                          
    time.sleep(5)                     