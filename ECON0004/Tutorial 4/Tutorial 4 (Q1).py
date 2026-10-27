import matplotlib.pyplot as plt
import numpy as np

# Data
group_a_before = 23.25  # Control group (no criminal record), 2017
group_a_after = 20.37   # Control group (no criminal record), 2019
group_b_before = 49.46  # Treatment group (criminal record), 2017
group_b_after = 42.86   # Treatment group (criminal record), 2019

# DiD Calculation
delta_a = group_a_after - group_a_before  # Change in control group
delta_b = group_b_after - group_b_before  # Change in treatment group
did_estimator = delta_b - delta_a         # Difference-in-differences

print("=" * 45)
print("   DIFFERENCE-IN-DIFFERENCES ESTIMATION")
print("=" * 45)
print(f"\nGroup A (Control) change:  {group_a_after}% - {group_a_before}% = {delta_a:.2f}pp")
print(f"Group B (Treatment) change: {group_b_after}% - {group_b_before}% = {delta_b:.2f}pp")
print(f"\nDiD Estimator: {delta_b:.2f} - ({delta_a:.2f}) = {did_estimator:.2f} pp")
print(f"\n→ The policy reduced unemployment by {abs(did_estimator):.2f} percentage points")

# Counterfactual for Group B (what would have happened without the policy)
group_b_counterfactual = group_b_before + delta_a

# --- Plot ---
years = [2017, 2019]

fig, ax = plt.subplots(figsize=(9, 6))

# Actual lines
ax.plot(years, [group_a_before, group_a_after], 'bo-', linewidth=2.5,
        markersize=8, label='Group A (Control – No criminal record)')
ax.plot(years, [group_b_before, group_b_after], 'rs-', linewidth=2.5,
        markersize=8, label='Group B (Treatment – Criminal record)')

# Counterfactual line (dashed)
ax.plot(years, [group_b_before, group_b_counterfactual], 'r--', linewidth=2,
        markersize=8, label='Group B Counterfactual (without policy)')

# Annotate DiD arrow
ax.annotate('', xy=(2019, group_b_after), xytext=(2019, group_b_counterfactual),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2.5))
ax.text(2019.03, (group_b_after + group_b_counterfactual) / 2,
        f'DiD = {did_estimator:.2f}pp', color='green', fontsize=11, va='center')

# Shade the DiD region
ax.fill_between([2019, 2019], group_b_after, group_b_counterfactual,
                alpha=0.15, color='green')

# Labels at endpoints
for x, y, label in [
    (2017, group_a_before, f'{group_a_before}%'),
    (2019, group_a_after,  f'{group_a_after}%'),
    (2017, group_b_before, f'{group_b_before}%'),
    (2019, group_b_after,  f'{group_b_after}%'),
    (2019, group_b_counterfactual, f'{group_b_counterfactual:.2f}%\n(counterfactual)'),
]:
    ax.annotate(label, xy=(x, y), xytext=(x - 0.05, y + 1.2), fontsize=9, color='gray')

# Formatting
ax.set_xticks([2017, 2019])
ax.set_xticklabels(['2017 (Before)', '2019 (After)'], fontsize=12)
ax.set_ylabel('Unemployment Rate (%)', fontsize=12)
ax.set_title('Difference-in-Differences Estimator\nEffect of Employment Rehabilitation Policy', fontsize=13)
ax.legend(fontsize=10, loc='upper right')
ax.set_ylim(10, 60)
ax.set_xlim(2016.7, 2019.6)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('did_plot.png', dpi=150)
plt.show()