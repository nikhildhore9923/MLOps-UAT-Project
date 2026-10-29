
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Reference data: original dataset
reference_data = pd.DataFrame({
    "age": [22, 25, 28, 30, 32, 35, 27, 29, 31, 26],
    "salary": [25000, 28000, 32000, 35000, 38000, 42000, 30000, 33000, 36000, 29000]
})

# Current data: data to monitor
current_data = pd.DataFrame({
    "age": [40, 42, 45, 43, 41, 46, 44, 42, 47, 45],
    "salary": [50000, 52000, 55000, 53000, 51000, 58000, 54000, 52000, 60000, 56000]
})

# Generate data drift report
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference_data, current_data=current_data)
report.save_html("evidently_report.html")

print("Evidently report generated: evidently_report.html")
