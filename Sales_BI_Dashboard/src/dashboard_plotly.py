import plotly.express as px

def create_interactive_dashboard(df):

    fig = px.line(df, x="month", y="revenue",
                  title="Interactive Revenue Trend",
                  markers=True)

    fig.show()