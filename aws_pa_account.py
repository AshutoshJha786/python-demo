
import boto3
import argparse
import logging


def artifact_version():
    response_for_version = client.describe_product(
        AcceptLanguage='en',
        Name='ApplicationTeams'
    )
    versions_list=[]
    for each_data in response_for_version['ProvisioningArtifacts']:
        versions_list.append(each_data['Id'])
    Artifact_latest_version_Id=versions_list[len(versions_list)-1]
    return Artifact_latest_version_Id

def provision_product(version):
    try:

        client.provision_product(
                AcceptLanguage='en',
                ProductName="ApplicationTeams",
                ProvisioningArtifactId=version,
                ProvisionedProductName=args.ProvisionedProductName,
                ProvisioningParameters=[
                    {
                        'Key': 'pName',
                        'Value': args.Name
                    },
                    {
                        'Key': 'pChargeCode',
                        'Value': args.ChargeCode
                    },
                    {
                        'Key': 'pProductId',
                        'Value': args.ProductId
                    },
                    {
                        'Key': 'pEmailAddress',
                        'Value': args.EmailAddress
                    },
                ],
        )
    except Exception as error:
        logging.error(error)

if __name__=='__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s',filename='log_provision.txt',level=logging.INFO)

# Input for provisioned_product_name, ProductId, ChargeCode, Name and Email address

    parser = argparse.ArgumentParser()
    parser.add_argument("ProvisionedProductName")
    parser.add_argument("Name")
    parser.add_argument("ChargeCode")
    parser.add_argument("ProductId")
    parser.add_argument("EmailAddress")

    args = parser.parse_args()

    #getting latest version of product
    client = boto3.client('servicecatalog')
    version=artifact_version()
    provision_product(version)

