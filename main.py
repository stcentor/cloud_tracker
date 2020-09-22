import sys


def main(dict):
    import smtplib, ssl
    from platform_services import GlobalTaggingV1
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    
    authenticator = IAMAuthenticator('kPKHngCU7xNXcoZMEdvJ6PHG5GTQzX8jmFS-Lpg5jry4')
    global_tagging = GlobalTaggingV1(authenticator=authenticator)
    
    resource = {}
    resource['resource_id'] = 'crn:v1:bluemix:public:containers-kubernetes:us-south:a/10d5953a4ae3bcb588e62b724aa43d70:bpts5vad0lnqunih8lo0::'
    resources = [ resource ]
    
    env = global_tagging.attach_tag('testskyler', resources)
    result = env.get_result()
    
    results = result.get('results')
    print(results[0].is_error)

    port = 465  # For SSL
    password = ""
    sender_email = ""
    receiver_email = ""
    message = dict
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("skyler.tangneycentor@gmail.com", password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)

    for item in  dict:
        print(item)
        #search for tags
    
    return { 'message': dict }
