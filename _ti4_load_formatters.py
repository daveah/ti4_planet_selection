#!/usr/bin/env python


# Return tile information
def _ti4_load_formatters():
    return {
        "Text": {
            "Title Pre": "",
            "Title Post": "\n",
            "Table Pre": "",
            "System Pre": "  ",
            "Col1 Pre": "Name: ",
            "Col2 Pre": "; Resource: ",
            "Col3 Pre": "; Influence: ",
            "Col4 Pre": "; ",
            "Col5 Pre": "",
            "Col6 Pre": "",
            "System Post": "\n",
            "Table Post": "",
            "Summary Pre": "  ",
            "Summary Post": "\n",
            "Planet Formatter": "{:22}",
            "Error Pre": "",
            "Error Post": "\n",
        },
        "HTML": {
            "Title Pre": "<h2>",
            "Title Post": "</h2>",
            "Table Pre": (
                "<table><tr>" +
                "<th>System Name</th>" +
                "<th>Resources</th>" +
                "<th>Influence</th>" +
                "<th>Wormhole</th>" +
                "<th>Anomaly</th>" +
                "<th>Blank</th>" +
                "</tr>"
            ),
            "System Pre": "<tr><td>",
            "Col1 Pre": "",
            "Col2 Pre": "</td><td>",
            "Col3 Pre": "</td><td>",
            "Col4 Pre": "</td><td>",
            "Col5 Pre": "</td><td>",
            "Col6 Pre": "</td><td>",
            "System Sep": "",
            "System Post": "</td></tr>",
            "Table Post": "</table>",
            "Summary Pre": "<p><i>",
            "Summary Post": "</i></p>",
            "Planet Formatter": "{}",
            "Error Pre": "<h2>Error</h2><p>",
            "Error Post": "</p>",
        },
    }
