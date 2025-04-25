import streamlit as st
import numpy as np 

# Assuming you have your spam function and the necessary variables defined
spam_words = {'free': 100, 'win': 150, 'cash': 120}  # Example
ham_words = {'hello': 200, 'meeting': 250, 'urgent': 180}  # Example
all_words = {'free': 200, 'win': 250, 'cash': 220, 'hello': 300, 'meeting': 350, 'urgent': 300}  # Example

def process_message(message):
    # Simple word processing function (you can adjust this for real processing)
    return message.lower().split()

def spam(message, s=1, p=0.5, percentage=False):
    n = 0
    spam_freq = 0
    ham_freq = 0
    for word in process_message(message):
        if word in spam_words:
            spam_freq = (spam_words[word] / all_words[word])

        if word in ham_words:
            ham_freq = (ham_words[word] / all_words[word])

        if not (spam_freq + ham_freq) == 0 and word in all_words:
            spaminess_of_word = (spam_freq) / (spam_freq + ham_freq)
            corr_spaminess = (s * p + all_words[word] * spaminess_of_word) / (s + all_words[word])
            n += np.log(1 - corr_spaminess) - np.log(corr_spaminess)

    spam_result = 1 / (1 + np.e**n)

    if percentage:
        return spam_result * 100
    elif spam_result > 0.5:
        return True
    else:
        return False

# Streamlit user interface
def main():
    st.title("Spam Message Detection")
    
    # Input message
    message = st.text_area("Enter your message here:")
    
    # Option to display result as a percentage
    percentage = st.checkbox("Show result as percentage")
    
    if st.button("Check if Spam"):
        if message:
            spam_result = spam(message, percentage=percentage)
            if percentage:
                st.write(f"Spam probability: {spam_result:.2f}%")
            else:
                if spam_result:
                    st.write("This message is likely SPAM.")
                else:
                    st.write("This message is NOT SPAM.")
        else:
            st.error("Please enter a message!")

# Run the app
# to run use the below command.
# streamlit run spamGui.py
if __name__ == "__main__":
    main()