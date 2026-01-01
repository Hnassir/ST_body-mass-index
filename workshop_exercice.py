# BMI calculator

import streamlit as st

st.title('Welcome to BMI Calculator',text_alignment='center')

st.space(size='small')

weight = st.number_input('enter your weight (in kgs)',min_value=0.0)


st.space(size='small')

format =st.radio('choose your height format : ',options=['meters','feet','cms'], horizontal=True)

st.space(size='small')


if format =='cms':
    height=st.number_input('enter your height in centimeters',min_value=0.0)
    try :
        bmi=weight/((height/100)**2)
    except:
        st.warning('must enter height')

elif format =='meters':
    height=st.number_input('enter your height in meters',min_value=0.0)
    try :
        bmi=weight/((height)**2)
    except:
        st.warning('must enter height')

else :
    height=st.number_input('enter your height in feet',min_value=0.0)
    try :
        bmi=weight/((height*0.3048)**2)
    except:
        st.warning('must enter height')

st.space(size='small')

if(st.button('Run BMI (Body Mass Index) Calculation')):

    st.write('your bmi Index is : ',bmi,'KG/m^2')

    if bmi <16:
        st.error('You are extremly underweight')
    elif bmi >=16:
        st.warning('You are underweight')
    elif bmi>=18.5 and bmi<25:
        st.success('You are healthy')
    elif bmi>=25 and bmi<30:
        st.warning('You are overweight')
    elif bmi>=30 :
        st.error('You are extremly overweight')


    