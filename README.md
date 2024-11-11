# treat-tracker
(Learning Project) Expense tracker built using Python/Flask on the Backend and React on the Frontend

## Overal Design Description:
Treat-Tracker will be a webiste that allows a user to input their expenditures into a database/table and view insights into their financial trends (e.g. graphs and charts)

### Database
Treat-Tracker will be a webiste that allows a user to input their expenditures into a database/table. Expenditures will be identified by a unique ID number and contain information about the cost, date, category, and description of the purchase. The expenditures table will by default be sorted by date, and optionally sorted by cost or category. The user will be able to filter the table by min-max date or cost, as well as by category. (Maybe the user can search for keywords in descriptions).

### Insights
Treat tracker will allow the user to see figures that provide insights into their financial habits and trends. For now, my plan is to start out simple with a bar graph with weekly, monthly, and yearly time intervals, and a pie chart separating categoires by cost, with both figures adjustable by date range.
