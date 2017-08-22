from connect import SQLTESTS

if __name__ == '__main__':

    q = SQLTESTS()
    q.test_purchases()
    q.test_visits()
    q.test_two_global_segments()
    q.number_of_new_special_clients()
    q.number_of_class_based_clients()
    q.number_of_memberships_clients()
    q.number_of_3rd_party_clients()
    q.number_of_inactive_clients()
    q.number_of_inactive_with_creds_clients()
    q.class_based_users_purchases_visits()
    q.membership_users_purchases()
    q.membership_users_visits()
    q.inactive_users_have_no_visits()
    q.inactive_users_have_no_purchases()
    q.number_of_class_based_clients1()
    q.number_of_memberships_clients1()
    q.number_of_3rd_party_clients1()
    q.inactive_users_no_activity()
