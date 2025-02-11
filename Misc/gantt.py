import plotly.figure_factory as ff
import pandas as pd

df = pd.DataFrame([
    dict(Task="Initial Dataset Collection", Start=0, Finish=2),
    dict(Task="LLM Prompt Development & Fine-Tuning", Start=2, Finish=14),
    dict(Task="Backend Engine and WebUI Development", Start=6, Finish=18),
    dict(Task="Evaluation and Testing", Start=16, Finish=24),
    dict(Task="Thesis Writing", Start=0, Finish=26)
])

# fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
# fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
# fig.show()

# fig = ff.create_gantt(df, index_col = 'Resource',  bar_width = 0.4, show_colorbar=True)
fig = ff.create_gantt(df, bar_width = 0.4, title="Thesis Timeline", showgrid_x=True)
fig.update_layout(xaxis_type='linear', width=1000, height=420)
fig.layout.xaxis['tickvals'] = list(range(0, 27, 2))
fig.layout.xaxis['title'] = "Week Number"
# fig.show()

fig.write_image("draft_timeline.png", scale=2.5)