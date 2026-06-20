def get_company_name(filename: str):

    filename = filename.lower()

    if "apple" in filename:
        return "Apple"

    if "microsoft" in filename:
        return "Microsoft"

    if "nvidia" in filename:
        return "Nvidia"

    if "fomc" in filename:
        return "Federal Reserve"

    if "monetary" in filename:
        return "Federal Reserve"

    return "Unknown"


def get_document_type(filename: str):

    filename = filename.lower()

    if "10k" in filename:
        return "10-K"

    if "fomc" in filename:
        return "FOMC Minutes"

    if "monetary" in filename:
        return "Monetary Policy Report"

    return "Unknown"