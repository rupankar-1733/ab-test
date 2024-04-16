import streamlit as st
import scipy.stats as stats

# Function to perform A/B test
def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates
    control_conversion_rate = control_conversions / control_visitors
    treatment_conversion_rate = treatment_conversions / treatment_visitors
    
    # Calculate z-score
    z_score = (treatment_conversion_rate - control_conversion_rate) / \
              ((control_conversion_rate * (1 - control_conversion_rate) / control_visitors) + \
               (treatment_conversion_rate * (1 - treatment_conversion_rate) / treatment_visitors))**0.5
    
    # Determine critical z-value based on confidence level
    if confidence_level == 90:
        critical_z_value = stats.norm.ppf(0.95)
    elif confidence_level == 95:
        critical_z_value = stats.norm.ppf(0.975)
    elif confidence_level == 99:
        critical_z_value = stats.norm.ppf(0.995)
    else:
        raise ValueError("Confidence level must be 90, 95, or 99")
    
    # Compare z-score with critical z-value and output result
    if z_score > critical_z_value:
        return "Experiment Group is Better"
    elif z_score < -critical_z_value:
        return "Control Group is Better"
    else:
        return "Indeterminate"

def main():
    st.title('A/B Test Hypothesis Test')
    
    # User inputs
    control_visitors = st.number_input('Control Group Visitors', min_value=1, step=1)
    control_conversions = st.number_input('Control Group Conversions', min_value=0, step=1)
    treatment_visitors = st.number_input('Treatment Group Visitors', min_value=1, step=1)
    treatment_conversions = st.number_input('Treatment Group Conversions', min_value=0, step=1)
    confidence_level = st.select_slider('Confidence Level', options=[90, 95, 99])
    
    # Perform A/B test when user clicks the button
    if st.button('Perform A/B Test'):
        result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.write('Result of A/B test:', result)

if __name__ == '__main__':
    main()