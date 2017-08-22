import psycopg2
import xlsxwriter
import random
from random import randrange

class SQLTESTS():

    def __init__(self):
        """ Connect to the PostgreSQL database server """
        self.conn = None

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        self.conn = psycopg2.connect(host="",
                                     port="",database="", user="", password="")
        self.workbook = xlsxwriter.Workbook('test.xlsx')

    def test_purchases(self):


        # create a cursor
        cur = self.conn.cursor()
        cur.execute('''SELECT * FROM purchases
                        WHERE created_at::timestamp::date = NOW()::timestamp::date
                        OR updated_at::timestamp::date = NOW()::timestamp::date''')
        purchases = cur.fetchall()

        worksheet1 = self.workbook.add_worksheet()
        worksheet1.name = 'ALL.purchases'

        worksheet1.write('A1', 'id')
        worksheet1.write('B1', 'mbid')
        worksheet1.write('C1', 'datetime')
        worksheet1.write('D1', 'name')
        worksheet1.write('E1', 'total_price')
        worksheet1.write('F1', 'created_at')
        worksheet1.write('G1', 'updated_at')
        worksheet1.write('H1', 'service_id')
        worksheet1.write('I1', 'user_id')
        i = 2
        for p in purchases:
            worksheet1.write('A{0}'.format(i), p[0])
            worksheet1.write('B{0}'.format(i), p[1])
            worksheet1.write('C{0}'.format(i), str(p[2]))
            worksheet1.write('D{0}'.format(i), p[3])
            worksheet1.write('E{0}'.format(i), p[4])
            worksheet1.write('F{0}'.format(i), str(p[5]))
            worksheet1.write('G{0}'.format(i), str(p[6]))
            worksheet1.write('H{0}'.format(i), p[7])
            worksheet1.write('I{0}'.format(i), p[8])
            i+=1
            cur.close()
    def test_visits(self):

        cur = self.conn.cursor()
        cur.execute('''SELECT * FROM purchases
                        WHERE created_at::timestamp::date = (NOW() - interval '12 hours')::timestamp::date
                        OR updated_at::timestamp::date = (NOW() - interval '12 hours')::timestamp::date''')
        visits = cur.fetchall()

         # close the communication with the PostgreSQL

        worksheet2 = self.workbook.add_worksheet()
        worksheet2.name = 'ALL.visits'

        worksheet2.write('A1', 'id')
        worksheet2.write('B1', 'datetime')
        worksheet2.write('C1', 'klass')
        worksheet2.write('D1', 'created_at')
        worksheet2.write('E1', 'updated_at')
        worksheet2.write('F1', 'user_id')
        f = 2
        for v in visits:
            worksheet2.write('A{0}'.format(f), v[0])
            worksheet2.write('B{0}'.format(f), str(v[1]))
            worksheet2.write('C{0}'.format(f), v[2])
            worksheet2.write('D{0}'.format(f), str(v[3]))
            worksheet2.write('E{0}'.format(f), str(v[4]))
            worksheet2.write('F{0}'.format(f), v[5])
            f+=1

    def test_two_global_segments(self):


        cur = self.conn.cursor()
        cur.execute("SELECT users.id, COUNT(global_segments_users.global_segment_id) FROM users "
                    "INNER JOIN global_segments_users ON global_segments_users.user_id = users.id "
                    "GROUP BY users.id "
                    "HAVING COUNT(global_segments_users.global_segment_id) > 1")
        two_global_segments = cur.fetchall()

        worksheet3 = self.workbook.add_worksheet()
        worksheet3.name = '2Globals'

        worksheet3.write('A1', 'id')
        worksheet3.write('B1', 'count')
        x = 2
        for g in two_global_segments:
            worksheet3.write('A{0}'.format(x), g[0])
            worksheet3.write('B{0}'.format(x), str(g[1]))
            x+=1
        cur.close()


    def number_of_new_special_clients(self):

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 2 and studio_id = 5")

        special_clients = cur.fetchall()

        worksheet4 = self.workbook.add_worksheet()
        worksheet4.name = 'CountNSC'

        worksheet4.write('A1', 'NumberOfUsers')
        z = 2
        print(z)
        for e in special_clients:
            worksheet4.write('A{0}'.format(z), str(e[0]))
            z+=1

    def number_of_class_based_clients(self):

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 3 and studio_id = 5")

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'CountCBC'

        worksheet5.write('A1', 'NumberOfUsers')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            z+=1

    def number_of_memberships_clients(self):

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 4 and studio_id = 5")

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'CountMC'

        worksheet5.write('A1', 'NumberOfUsers')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            z+=1

    def number_of_3rd_party_clients(self):

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 5 and studio_id = 5")

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'Count3rdC'

        worksheet5.write('A1', 'NumberOfUsers')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            z+=1

    def number_of_inactive_clients(self):

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 6 and studio_id = 5")

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'CountIC'

        worksheet5.write('A1', 'NumberOfUsers')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            z+=1

    def number_of_inactive_with_creds_clients(self):

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 7 and studio_id = 5")

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'CountIWCC'

        worksheet5.write('A1', 'NumberOfUsers')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            z+=1

    def class_based_users_purchases_visits(self):

        cur = self.conn.cursor()
        cur.execute('''SELECT users.id user_id, users.studio_id, purchases.id purchase_id, purchases.datetime, COUNT(visits.datetime) count_visits, global_segments_users.global_segment_id FROM users
                    INNER JOIN global_segments_users ON users.id = global_segments_users.user_id
                    RIGHT JOIN purchases ON users.id = purchases.user_id
                    RIGHT JOIN visits ON users.id = visits.user_id
                    WHERE purchases.datetime::timestamp::date > NOW() - interval '30 days'
                    AND visits.datetime::timestamp::date > NOW() - interval '30 days'
                    AND global_segment_id = 3
                    AND users.studio_id = 5
                    GROUP BY purchases.id, users.id, users.studio_id, purchases.id, purchases.datetime, global_segments_users.global_segment_id''')

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'purchases and visits CBC'

        worksheet5.write('A1', 'user_id')
        worksheet5.write('B1', 'studio_id')
        worksheet5.write('C1', 'purchase_id')
        worksheet5.write('D1', 'datetime')
        worksheet5.write('E1', 'count_visits')
        worksheet5.write('F1', 'global_segment_id')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            worksheet5.write('B{0}'.format(z), str(e[1]))
            worksheet5.write('C{0}'.format(z), str(e[2]))
            worksheet5.write('D{0}'.format(z), str(e[3]))
            worksheet5.write('E{0}'.format(z), str(e[4]))
            worksheet5.write('F{0}'.format(z), str(e[5]))
            z+=1

    def membership_users_purchases(self):

        cur = self.conn.cursor()
        cur.execute('''SELECT users.id user_id, users.studio_id, count(p.datetime) purchases, s.category, global_segments_users.global_segment_id FROM users
                    INNER JOIN global_segments_users ON users.id = global_segments_users.user_id
                    INNER JOIN purchases p ON users.id = p.user_id
                    INNER JOIN services s on s.id = p.service_id
                    WHERE global_segment_id = 4
                    AND s.category = 3
                    AND users.studio_id = 5
                    AND p.datetime::timestamp::date > NOW() - interval '365 days'
                    GROUP BY users.id, users.studio_id, global_segments_users.global_segment_id, s.category''')

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'M.purchases'

        worksheet5.write('A1', 'user_id')
        worksheet5.write('B1', 'studio_id')
        worksheet5.write('C1', 'purchases')
        worksheet5.write('D1', 'category')
        worksheet5.write('E1', 'global_segment_id')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            worksheet5.write('B{0}'.format(z), str(e[1]))
            worksheet5.write('C{0}'.format(z), str(e[2]))
            worksheet5.write('D{0}'.format(z), str(e[3]))
            worksheet5.write('E{0}'.format(z), str(e[4]))
            z+=1

    def membership_users_visits(self):

        cur = self.conn.cursor()
        cur.execute('''SELECT users.id user_id, users.studio_id, count(v.datetime) visits, s.category, global_segments_users.global_segment_id FROM users
                    INNER JOIN global_segments_users ON users.id = global_segments_users.user_id
                    INNER JOIN visits v ON users.id = v.user_id
                    INNER JOIN purchases p ON users.id = p.user_id
                    INNER JOIN services s on s.id = p.service_id
                    WHERE global_segment_id = 4
                    AND s.category = 3
                    AND users.studio_id = 5
                    AND v.datetime::timestamp::date > NOW() - interval '30 days'
                    GROUP BY users.id, users.studio_id, global_segments_users.global_segment_id, s.category''')

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'M.visits'

        worksheet5.write('A1', 'user_id')
        worksheet5.write('B1', 'studio_id')
        worksheet5.write('C1', 'visits')
        worksheet5.write('D1', 'category')
        worksheet5.write('E1', 'global_segment_id')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            worksheet5.write('B{0}'.format(z), str(e[1]))
            worksheet5.write('C{0}'.format(z), str(e[2]))
            worksheet5.write('D{0}'.format(z), str(e[3]))
            worksheet5.write('E{0}'.format(z), str(e[4]))
            z+=1

    def inactive_users_have_no_visits(self):

        cur = self.conn.cursor()
        cur.execute('''SELECT users.id user_id, users.studio_id, COUNT(visits.datetime) count_visits, global_segments_users.global_segment_id FROM users
                    INNER JOIN global_segments_users ON users.id = global_segments_users.user_id
                    RIGHT JOIN visits ON users.id = visits.user_id
                    WHERE visits.datetime::timestamp::date > NOW() - interval '30 days'
                    AND global_segment_id = 6
                    AND users.studio_id = 5
                    GROUP BY users.id, users.studio_id, visits.datetime, global_segments_users.global_segment_id''')

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'I.NoVisits'

        worksheet5.write('A1', 'user_id')
        worksheet5.write('B1', 'studio_id')
        worksheet5.write('C1', 'count_visits')
        worksheet5.write('D1', 'global_segment_id')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            worksheet5.write('B{0}'.format(z), str(e[1]))
            worksheet5.write('C{0}'.format(z), str(e[2]))
            worksheet5.write('D{0}'.format(z), str(e[3]))
            z+=1

    def inactive_users_have_no_purchases(self):

        cur = self.conn.cursor()
        cur.execute('''SELECT users.id user_id, users.studio_id, purchases.id purchase_id, purchases.datetime, global_segments_users.global_segment_id FROM users
                    INNER JOIN global_segments_users ON users.id = global_segments_users.user_id
                    RIGHT JOIN purchases ON users.id = purchases.user_id
                    WHERE purchases.datetime::timestamp::date > NOW() - interval '30 days'
                    AND service_id is not null
                    AND global_segment_id = 6
                    AND users.studio_id = 5
                    GROUP BY purchases.id, users.id, users.studio_id, purchases.id, purchases.datetime, purchases.total_price, global_segments_users.global_segment_id''')

        special_clients = cur.fetchall()

        worksheet5 = self.workbook.add_worksheet()
        worksheet5.name = 'I.Nopurchases'

        worksheet5.write('A1', 'user_id')
        worksheet5.write('B1', 'studio_id')
        worksheet5.write('C1', 'purchases_id')
        worksheet5.write('D1', 'datetime')
        worksheet5.write('E1', 'global_segment_id')
        z = 2
        for e in special_clients:
            worksheet5.write('A{0}'.format(z), str(e[0]))
            worksheet5.write('B{0}'.format(z), str(e[1]))
            worksheet5.write('C{0}'.format(z), str(e[2]))
            worksheet5.write('D{0}'.format(z), str(e[3]))
            worksheet5.write('E{0}'.format(z), str(e[4]))
            z+=1

    def number_of_class_based_clients1(self):

        cur = self.conn.cursor()
        cur.execute("SELECT user_id FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 3 and studio_id = 5")

        special_clients = cur.fetchall()

        user_id = special_clients
        # random_index = randrange(0,len(user_id))
        random_idxs = list([random.choice(user_id)[0] for _ in range(2)])
        print(random_idxs)
        # user_one = user_id[random_index]

        # a = int(user_id[random_index][0])
        # print(a)
        for i, idx in enumerate(random_idxs):

            cur.execute('''SELECT u.id user_id, p.id purchase_id, p.name name_of_purchase, p.datetime when_was_purchased, count(v.datetime) visits_count  FROM users u
                        INNER JOIN purchases p on p.user_id = u.id
                        INNER JOIN visits v on v.user_id = u.id
                        WHERE u.id = ''' + "'{0}'".format(idx) +
                        '''AND p.datetime::timestamp::date > NOW() - interval '30 days'
                        AND v.datetime::timestamp::date > NOW() - interval '30 days'
                        GROUP BY u.id, p.id, p.name, p.datetime''')

            class_based_clients = cur.fetchall()

            worksheet5 = self.workbook.add_worksheet()
            worksheet5.name = 'test' + str(i)

            worksheet5.write('A1', 'user_id')
            worksheet5.write('B1', 'purchase_id')
            worksheet5.write('C1', 'name_of_purchase')
            worksheet5.write('D1', 'when_was_purchased')
            worksheet5.write('E1', 'visits_count')
            z = 2
            for e in class_based_clients:
                worksheet5.write('A{0}'.format(z), str(e[0]))
                worksheet5.write('B{0}'.format(z), str(e[1]))
                worksheet5.write('C{0}'.format(z), str(e[2]))
                worksheet5.write('D{0}'.format(z), str(e[3]))
                worksheet5.write('E{0}'.format(z), str(e[4]))
                z +=1

    def number_of_memberships_clients1(self):

        cur = self.conn.cursor()
        cur.execute("SELECT user_id FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 4 and studio_id = 5")

        special_clients = cur.fetchall()

        user_id = special_clients
        random_idxs = list([random.choice(user_id)[0] for _ in range(2)])
        print(random_idxs)
        for i, idx in enumerate(random_idxs):

            cur.execute('''SELECT u.id user_id, p.id purchase_id, p.name name_of_purchase, p.datetime when_was_purchased, count(v.datetime) visits_count, services.category  FROM users u
                        INNER JOIN purchases p on p.user_id = u.id
                        INNER JOIN visits v on v.user_id = u.id
                        INNER JOIN services on services.id = p.service_id
                        WHERE u.id = ''' + "'{0}'".format(idx) +
                        '''AND p.datetime::timestamp::date > NOW() - interval '365 days'
                        AND services.category = 3
                        AND v.datetime::timestamp::date > NOW() - interval '30 days'
                        GROUP BY u.id, p.id, p.name, p.datetime, services.category''')

            class_based_clients = cur.fetchall()

            worksheet5 = self.workbook.add_worksheet()
            worksheet5.name = 'memberships' + str(i)

            worksheet5.write('A1', 'user_id')
            worksheet5.write('B1', 'purchase_id')
            worksheet5.write('C1', 'name_of_purchase')
            worksheet5.write('D1', 'when_was_purchased')
            worksheet5.write('E1', 'visits_count')
            worksheet5.write('F1', 'category')
            z = 2
            for e in class_based_clients:
                worksheet5.write('A{0}'.format(z), str(e[0]))
                worksheet5.write('B{0}'.format(z), str(e[1]))
                worksheet5.write('C{0}'.format(z), str(e[2]))
                worksheet5.write('D{0}'.format(z), str(e[3]))
                worksheet5.write('E{0}'.format(z), str(e[4]))
                worksheet5.write('F{0}'.format(z), str(e[5]))
                z +=1

    def number_of_3rd_party_clients1(self):

        cur = self.conn.cursor()
        cur.execute("SELECT user_id FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 5 and studio_id = 5")

        special_clients = cur.fetchall()

        user_id = special_clients
        random_idxs = list([random.choice(user_id)[0] for _ in range(2)])
        print(random_idxs)
        for i, idx in enumerate(random_idxs):

            cur.execute('''SELECT u.id user_id, p.id purchase_id, p.name name_of_purchase, p.datetime when_was_purchased, count(v.datetime) visits_count, services.category  FROM users u
                        INNER JOIN purchases p on p.user_id = u.id
                        INNER JOIN visits v on v.user_id = u.id
                        INNER JOIN services on services.id = p.service_id
                        WHERE u.id = ''' + "'{0}'".format(idx) +
                        '''AND p.datetime::timestamp::date > NOW() - interval '30 days'
                        AND services.category = 2
                        AND v.datetime::timestamp::date > NOW() - interval '30 days'
                        GROUP BY u.id, p.id, p.name, p.datetime, services.category''')

            class_based_clients = cur.fetchall()

            worksheet5 = self.workbook.add_worksheet()
            worksheet5.name = '3rdParties' + str(i)

            worksheet5.write('A1', 'user_id')
            worksheet5.write('B1', 'purchase_id')
            worksheet5.write('C1', 'name_of_purchase')
            worksheet5.write('D1', 'when_was_purchased')
            worksheet5.write('E1', 'visits_count')
            worksheet5.write('F1', 'category')
            z = 2
            for e in class_based_clients:
                worksheet5.write('A{0}'.format(z), str(e[0]))
                worksheet5.write('B{0}'.format(z), str(e[1]))
                worksheet5.write('C{0}'.format(z), str(e[2]))
                worksheet5.write('D{0}'.format(z), str(e[3]))
                worksheet5.write('E{0}'.format(z), str(e[4]))
                worksheet5.write('F{0}'.format(z), str(e[5]))
                z +=1


    def inactive_users_no_activity(self):

        cur = self.conn.cursor()
        cur.execute("SELECT user_id FROM global_segments_users "
                    "INNER JOIN users ON users.id = global_segments_users.user_id "
                    "WHERE global_segment_id = 6 and studio_id = 5")

        inactive_clients = cur.fetchall()

        user_id = inactive_clients
        random_idxs = list([random.choice(user_id)[0] for _ in range(2)])
        print(random_idxs)
        for i, idx in enumerate(random_idxs):

            cur.execute('''SELECT users.id user_id, users.studio_id, purchases.id purchase_id, purchases.datetime was_purchased, visits.id visit_id, visits.datetime visit_datetime, global_segments_users.global_segment_id FROM users
                        INNER JOIN global_segments_users ON users.id = global_segments_users.user_id
                        INNER JOIN visits on visits.user_id = users.id
                        RIGHT JOIN purchases ON users.id = purchases.user_id
                        WHERE users.id = '''+ "'{0}'".format(idx) +
                        '''AND purchases.datetime::timestamp::date > NOW() - interval '30 days'
                        AND visits.datetime::timestamp::date > NOW() - interval '30 days'
                        AND service_id is not null
                        AND global_segment_id = 6
                        AND users.studio_id = 5
                        GROUP BY purchases.id, users.id, users.studio_id, purchases.id, purchases.datetime, purchases.total_price, visits.id, visits.datetime, global_segments_users.global_segment_id''')

            inactive_clients_rules = cur.fetchall()

            worksheet5 = self.workbook.add_worksheet()
            worksheet5.name = 'Inavtives' + str(i)

            worksheet5.write('A1', 'user_id')
            worksheet5.write('B1', 'studio_id')
            worksheet5.write('C1', 'purchase_id')
            worksheet5.write('D1', 'was_purchased')
            worksheet5.write('E1', 'visits_id')
            worksheet5.write('F1', 'visit_datetime')
            worksheet5.write('G1', 'global_segment_id')
            z = 2
            for e in inactive_clients_rules:
                worksheet5.write('A{0}'.format(z), str(e[0]))
                worksheet5.write('B{0}'.format(z), str(e[1]))
                worksheet5.write('C{0}'.format(z), str(e[2]))
                worksheet5.write('D{0}'.format(z), str(e[3]))
                worksheet5.write('E{0}'.format(z), str(e[4]))
                worksheet5.write('F{0}'.format(z), str(e[5]))
                worksheet5.write('G{0}'.format(z), str(e[5]))
                z +=1



        self.workbook.close()


