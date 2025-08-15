from datetime import date


def show_honor_dissmisal(counselor: str, effective_date: date, patient: str):
    letter = """
       <html>
                <head>
                    <title>Certificate of Accomplishment</title>
                </head>
                <body>
                    <h1>Certificate of Accomplishment</h1>
                    <p>From: {}
                    <p>Head, Counselor
                    <p>Date: {}
                    <br/>
                    <p>To: {}
                    <p>Subject: Termination of consultation
                    <br/>
                    <p>Dear {},
                    <p>&nbsp;&nbsp;It is with deep regret that we are informing you that we have decided to terminate you, 
                    <p>from our institution. This is for the reason of successive absences and non-complance to the rule of consultancy. 
                    <p>We also have to acquaint you with the reason for this decision. We wish you all the success in the future. (Cordially describe your greetings and requirements).
                    <p>Thank you.
                    <br/>

                    <p>Yours Sincerely,
                    <p>{}
                </body>
            </html>
    """.format(
        counselor, effective_date, patient, patient, counselor
    )
    return letter, 200
