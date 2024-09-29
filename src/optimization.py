from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, maximize, Reals


def optimize_stock(prices, predicted_demand, stock_capacity):
    model = ConcreteModel()

    model.stock = Var(prices.keys(), within=Reals, bounds=(0, None))

    model.profit = Objective(expr=sum(prices[i] * predicted_demand[i] * model.stock[i] for i in prices.keys()),
                             sense=maximize)

    model.stock_constraint = Constraint(expr=sum(model.stock[i] for i in prices.keys()) <= stock_capacity)

    solver = SolverFactory('glpk', executable='C:/glpk-4.65/w64/glpsol.exe')
    solver.solve(model)

    return {i: model.stock[i].value for i in prices.keys()}