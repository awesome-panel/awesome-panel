import pandas as pd


def get_chart_data():
        chart_data = {
            "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
            "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
        }
        return pd.DataFrame(chart_data)

def get_table_data():
        table_data = [
            (1001, "Lorem", "ipsum", "dolor", "sit"),
            (1002, "amet", "consectetur", "adipiscing", "elit"),
            (1003, "Integer", "nec", "odio", "Praesent"),
            (1003, "libero", "Sed", "cursus", "ante"),
            (1004, "dapibus", "diam", "Sed", "nisi"),
            (1005, "Nulla", "quis", "sem", "at"),
            (1006, "nibh", "elementum", "imperdiet", "Duis"),
            (1007, "sagittis", "ipsum", "Praesent", "mauris"),
            (1008, "Fusce", "nec", "tellus", "sed"),
            (1009, "augue", "semper", "porta", "Mauris"),
            (1010, "massa", "Vestibulum", "lacinia", "arcu"),
            (1011, "eget", "nulla", "Class", "aptent"),
            (1012, "taciti", "sociosqu", "ad", "litora"),
            (1013, "torquent", "per", "conubia", "nostra"),
            (1014, "per", "inceptos", "himenaeos", "Curabitur"),
            (1015, "sodales", "ligula", "in", "libero"),
        ]
        return pd.DataFrame(
            table_data, columns=["Header0", "Header1", "Header2", "Header3", "Header4"]
        ).set_index("Header0")
