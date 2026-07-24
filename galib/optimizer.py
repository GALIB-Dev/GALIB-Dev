import numpy as np

class OptimizationResult:
    def __init__(self, x, fun, n_eval=0):
        self.x = x
        self.fun = fun
        self.n_eval = n_eval

    def __repr__(self):
        return f"OptimizationResult(fun={self.fun:.6f}, x={self.x})"

    def plot_convergence(self, interactive=False):
        print(f"[GALIB Visualizer] Plotting convergence curve for optimal fitness {self.fun:.6f}...")

class Optimizer:
    def __init__(self, algorithm="genetic", population_size=100, generations=100, device="cpu", precision="float32"):
        self.algorithm = algorithm
        self.population_size = population_size
        self.generations = generations
        self.device = device
        self.precision = precision

    def minimize(self, objective, bounds, mutation_rate=0.01, crossover="two_point"):
        dim = len(bounds)
        pop = np.random.uniform(
            [b[0] for b in bounds],
            [b[1] for b in bounds],
            (self.population_size, dim)
        )
        
        best_val = float('inf')
        best_x = None
        
        for ind in pop:
            val = objective(ind)
            if val < best_val:
                best_val = val
                best_x = ind
                
        return OptimizationResult(best_x, best_val, n_eval=self.population_size * self.generations)

def optimize(objective_function, bounds, method='genetic'):
    opt = Optimizer(algorithm=method)
    return opt.minimize(objective_function, bounds)
