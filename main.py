import sys


def main(dict):
    import smtplib, ssl
    import os
    import pytest
    from ibm_cloud_sdk_core import ApiException, read_external_sources
    from ibm_platform_services.global_tagging_v1 import *


    config_file = 'global_tagging.env'



    global global_tagging_service
    if os.path.exists(config_file):
        os.environ['IBM_CREDENTIALS_FILE'] = config_file

        # begin-common

        global_tagging_service = GlobalTaggingV1.new_instance()

        # end-common
        assert global_tagging_service is not None

        # Load the configuration
        global config
        config = read_external_sources(
            GlobalTaggingV1.DEFAULT_SERVICE_NAME)

        global resource_crn
        resource_crn = config.get("RESOURCE_CRN")

    print('Setup complete.')

    needscredentials = pytest.mark.skipif(
    not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )


    try:
        # begin-attach_tag

        resource_model = {
            'resource_id': resource_crn
        }

        tag_results = global_tagging_service.attach_tag(
            resources=[resource_model],
            tag_names=['tag_test_1', 'tag_test_2']
        ).get_result()

        print(json.dumps(tag_results, indent=2))

        # end-attach_tag

    except ApiException as e:
        pytest.fail(str(e))

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
