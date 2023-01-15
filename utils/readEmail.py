import imaplib
import email
import traceback
import re
# import spacy
import os
import PyPDF2

# import en_core_sci_sm
from emailparser.models import Emails
from emailparser.serializers import EmailSerializer


class ReadEmail():
    ORG_EMAIL = "@gmail.com"
    FROM_EMAIL = "shahrukh.ali1496" + ORG_EMAIL
    # FROM_EMAIL = "maintenance@ta-trading.co.uk" #todo
    FROM_PWD = "hfouequsmtgukqpu"
    # FROM_PWD = "T3st1c@ll!!" #todo
    # SMTP_SERVER = "imap.secureserver.net"
    SMTP_SERVER = 'imap.gmail.com'
    SMTP_PORT = 993
    key_words = ['ISSUES:', 'Not Working', 'Reported']
    data = ""
    useful = False
    body_content = ""
    pdf_content = ""
    sender = ""
    subject = ""
    has_pdf = False
    task = False  # It will be true if data found

    @classmethod
    def read_pdf(cls, file_path):
        """
        For reading pdf body
        """
        cls.data = ""
        try:
            reader = PyPDF2.PdfReader(file_path)
            print(len(reader.pages))
            for page in reader.pages:
                cls.data + page.extract_text()
        except:
            cls.data = ""
        finally:
            return cls.data

    @classmethod
    def key_words_match(cls, body):
        cls.usefull = False
        try:
            text = body
            words = cls.key_words
            if len(text) > 0:
                sentences = [
                    sentence for sentence in text.split(".") if any(
                        w.lower() in sentence.lower() for w in words
                    )
                ]
                if sentences:
                    print("Working")
                    cls.usefull = True
        except Exception as ex:
            print("Exception occured in key Words Extraction and match")
        finally:
            return cls.useful

    @classmethod
    def fetch_sender(cls, raw_text):
        if ">" in raw_text:
            sender = ""
            try:
                sender = re.search(r'\<(.*?)\>', raw_text).group(1)
            except:
                sender = "Trouble getting sender email address"
            finally:
                return sender
        else:
            return raw_text

    @classmethod
    def read_email(cls):
        """
        Reading all unseen emails
        :return:
        """
        try:
            mail = imaplib.IMAP4_SSL(cls.SMTP_SERVER, int(cls.SMTP_PORT))
            mail.login(cls.FROM_EMAIL, cls.FROM_PWD)
            mail.select('INBOX')
            status, response = mail.search(None, '(UNSEEN)')
            mail_ids = response[0].split()
            first_email_id = int(mail_ids[0])
            latest_email_id = int(mail_ids[-1])
            cls.pdf_content = ""
            cls.body_content = ""
            # todo working with code for getting body
            for i in range(latest_email_id, first_email_id, -1):
                cls.body_content = ""  # For Email Body
                cls.pdf_content = ""  # For Pdf content if found
                cls.sender = ""  # email from
                cls.subject = ""  # Subject
                status, data = mail.fetch(str(i), '(RFC822)')
                email_msg = email.message_from_bytes(data[0][1])
                cls.sender = cls.fetch_sender(email_msg.get("From"))
                cls.subject = email_msg.get("subject")
                # Emails.objects.create(email_from=sender)
                if email_msg.is_multipart():
                    for part in email_msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            body = part.get_payload(decode=True)
                            try:
                                body = body.decode()
                            except:
                                continue # Iterate over new email data if found any exception
                            if cls.key_words_match(body):
                                cls.body_content = cls.body_content + body
                                cls.task = True
                        # elif content_type == "text/html":
                        #     continue
                        elif "attachment" in content_disposition:
                            filename = part.get_filename()
                            if filename:
                                # Change the path of directory
                                if not os.path.exists("/Users/mac/PycharmProjects/Crawlreap/email_folder"):
                                    # if the demo_folder directory is not present
                                    # then create it.
                                    os.makedirs("/Users/mac/PycharmProjects/Crawlreap/email_folder")
                                # folder_name = clean("test_email_downloads")
                                path_to_store_file = os.path.abspath(os.getcwd())
                                filepath = os.path.join("/Users/mac/PycharmProjects/Crawlreap/email_folder", filename)
                                # download attachment and save it
                                fp = open(filepath, 'wb')
                                fp.write(part.get_payload(decode=True))
                                fp.close()
                                text_data = cls.read_pdf(filepath)
                                text_data = re.sub(r'[^\x00-\x7f]', r'', text_data)
                                if cls.key_words_match(text_data):
                                    cls.pdf_content = cls.pdf_content + text_data
                                    cls.has_pdf = True
                                    cls.task = True
                if cls.task:
                    data = {"email_content": cls.body_content, "pdf_content": cls.pdf_content, "subject": cls.subject,
                            "has_pdf": cls.has_pdf,
                            "email_from": cls.sender}
                    serializer = EmailSerializer(data=data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                # todo working with code for getting body
        except Exception as e:
            traceback.print_exc()
            print(str(e))
