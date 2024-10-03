import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Set up the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login using the app password
server.login("sunitayadav190105@gmail.com", "lsph esqf cwnd kjgw")

# Create email content
msg = MIMEMultipart()
msg['From'] = "sunitayadav190105@gmail.com"
msg['To'] = "yadavnidhi190105@gmail.com"
msg['Subject'] = "Python Internship"

# Properly formatted email body text with new lines
body = """Dear Sunita,

Hope you are doing well.

Good to see you working on enhancing your skills and taking a step towards your career. 

Wishing you all the best for your internship!

Best Regards,
Sunita
"""

# Attach the body to the email
msg.attach(MIMEText(body, 'plain'))

# Add an attachment (replace 'file_path' with the actual path of your file)
file_path = "D:/Python_Internship/Python_Oct_Nov.pdf"  
attachment_name = os.path.basename(file_path)

# Open the file in binary mode and encode it
with open(file_path, "rb") as attachment:
    mime_base = MIMEBase('application', 'octet-stream')
    mime_base.set_payload(attachment.read())
    encoders.encode_base64(mime_base)

    # Add header for the attachment
    mime_base.add_header(
        'Content-Disposition',
        f'attachment; filename={attachment_name}'
    )

    # Attach the file to the email
    msg.attach(mime_base)

# Send the email
server.send_message(msg)

# Close the connection
server.quit()
print("Mail sent successfully")
