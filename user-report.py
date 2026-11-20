from veracode_api_py import Users
import pandas as pd

def get_account_type(user):
    if "@" in user["user_name"] and user["email_address"].startswith(user["user_name"]):
        return "API"
    else:
        return "Human"

def build_user(user):
    return {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email_address": user["email_address"],
        "saml": user["saml_user"],
        "last_login": user["last_login"] if "last_login" in user and user["last_login"] is not None else "Never",
        "last_ip": user["last_host"] if "last_host" in user and user["last_host"] is not None else "Never",

        "login_enabled": user["login_enabled"] if "login_enabled" in user else False,
        "ip_restritcted": user["ip_restricted"] if "ip_restricted" in user else False,
        "active": user["active"] if "active" in user else False,
        "account_type": get_account_type(user),
        "has_active_api_credentials": True if "api_credentials" in user else False,
        "api_credentials_expiration": user["api_credentials"]["expiration_ts"] if "api_credentials" in user and "expiration_ts" in user["api_credentials"] else None,
        "api_credentials_last_used": user["api_credentials"]["last_used_ts"] if "api_credentials" in user and "last_used_ts" in user["api_credentials"] else None,
        "deleted": user["deleted"] if "deleted" in user else False,
    }

def main():
    user_list = Users().get_all()
    if not user_list:
        print("No users found. It's likely that your API credentials are incorrect or you don't have access to the Veracode Identity APIs.")
        return

    full_user_info = [build_user(Users().get(user["user_id"])) for user in user_list if user["user_id"] is not None]

    user_rows = [user if isinstance(user, dict) else vars(user) for user in full_user_info]
    
    pd.DataFrame(user_rows).to_excel("users.xlsx", index=False)

if __name__ == "__main__":
    main()

    