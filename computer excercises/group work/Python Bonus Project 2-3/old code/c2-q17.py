"""
Auther     : Mohammad Mehdi Yadegarifard
Student ID : 810199308
Date       : 4-24-2022
Problem    : Problem 17
Discribe   : A city's temperature is modeled as a random variable with mean and
             standard deviation both equal to 10 degrees Celsius.
             A day is described as "normal" if the temperature during that day ranges
             within one standard deviation from the mean.
             What would be the temperature range for a normal day
             if temperature were expressed in degrees Fahrenheit? 
"""
import numpy as np
import matplotlib.pyplot as plt


def cel_to_fahr(cel_mu: float, cel_sigma: float) -> float:
    """
    since we know transform is linear, we can use the inverse transform
    fahr  = (cel * 9 / 5) + 32

    and new mean and sigma are:

    E[fahr] = (E[cel] * 9 / 5) + 32;

    var(fahr) = (9/5)^2 * var(cel)
    => sigma(fahr) = (9/5) * sigma(cel)

    """
    fahr_mu    = cel_mu * 9 / 5 + 32
    fahr_sigma = cel_sigma * 9 / 5

    return fahr_mu, fahr_sigma
    

def normal_pdf(x, mu:float, sigma:float) -> float:
    """
    normal distribution pdf function
    """
    return (1.0 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-0.5 * (x - mu) ** 2 / sigma ** 2)
    


def make_plot(axs, title: str, mu: float, sigma: float) -> None:
    """
    axs: matplotlib axes
    title: string
    mu: float
    sigma: float
    ------------------------
    We want to plot the distribution of the temperature
    and since we know it is normal, we can use the normal distribution function
    from scipy.stats.norm to plot it.
    for range of x, we use mu-3*sigma to mu+3*sigma
    to make sure we get a full range of the distribution.

    The normal range includes the Mu + - Sigma range, so we separate this area.
    """
    x     = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y     = normal_pdf(x, mu, sigma)
    left  = mu - sigma
    right = mu + sigma

    axs.plot(x, y, "k")
    axs.set_title(title, fontsize=14, loc="left")
    axs.vlines(left, 0,
        normal_pdf(left, mu, sigma),
        colors="r", linestyles="dashed")
    axs.text(
        left + (0.5 if left == 0 else 2),
        normal_pdf(left, mu, sigma) / 2,
        int(left),
        fontsize=10,
    )
    axs.vlines(right, 0,
        normal_pdf(right, mu, sigma),
        colors="r", linestyles="dashed")
    axs.text(
        right - (5 if right % 10 == 0 else 9),
        normal_pdf(right, mu, sigma) / 2,
        int(right),
        fontsize=10,
    )
    axs.spines["top"  ].set_visible(False)
    axs.spines["right"].set_visible(False)
    axs.spines["left" ].set_visible(False)
    axs.tick_params(left=False, labelleft=False)


def main():
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))
    
    celsius_mu    = 10
    celsius_sigma = 10
    
    fahrenheit_mu, fahrenheit_sigma = cel_to_fahr(celsius_mu, celsius_sigma)
    
    make_plot(
        axs[0], r"$\mathbf{Temperature \; in}$" +"\nCelsius",
        celsius_mu,
        celsius_sigma
    )
    make_plot(
        axs[1],
        r"$\mathbf{Temperature \; in}$" + "\nFahrenheit",
        fahrenheit_mu,
        fahrenheit_sigma,
    )
    plt.show()


if __name__ == "__main__":
    main()
