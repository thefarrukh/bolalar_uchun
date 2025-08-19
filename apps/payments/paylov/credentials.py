from apps.payments.models import ProviderCredentials, Providers


def get_credentials() -> dict[str, str | None]:
    """
    Get Paylov API credentials from the database and return as a dictionary.
    """
    paylov_provider = Providers.objects.filter(key="paylov").last()
    if not paylov_provider:
        raise ValueError("Paylov provider not found in database")

    paylov_creds = ProviderCredentials.objects.filter(provider=paylov_provider).all()
    print(paylov_creds)

    credentials = {
        "PAYLOV_API_KEY": getattr(
            paylov_creds.filter(key="PAYLOV_API_KEY").last(), "value", None
        ),
        "PAYLOV_USERNAME": getattr(
            paylov_creds.filter(key="PAYLOV_USERNAME").last(), "value", None
        ),
        "PAYLOV_PASSWORD": getattr(
            paylov_creds.filter(key="PAYLOV_PASSWORD").last(), "value", None
        ),
        "PAYLOV_SUBSCRIPTION_KEY": getattr(
            paylov_creds.filter(key="PAYLOV_SUBSCRIPTION_KEY").last(), "value", None
        ),
        "PAYLOV_REDIRECT_URL": getattr(
            paylov_creds.filter(key="PAYLOV_REDIRECT_URL").last(), "value", None
        ),
    }

    if not credentials["PAYLOV_REDIRECT_URL"] or not credentials["PAYLOV_API_KEY"]:
        raise ValueError("PAYLOV_REDIRECT_URL or PAYLOV_API_KEY is missing!")

    return credentials
