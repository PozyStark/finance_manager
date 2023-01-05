
export const barChartOptionsDashboard = {
  chart: {
    toolbar: {
      show: false,
    },
  },
  tooltip: {
    style: {
      fontSize: "10px",
      fontFamily: "Plus Jakarta Display",
    },
    onDatasetHover: {
      style: {
        fontSize: "10px",
        fontFamily: "Plus Jakarta Display",
      },
    },
    theme: "dark",
  },
  xaxis: {
    categories: ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    show: true,
    labels: {
      show: true,
      style: {
        colors: "#fff",
        fontSize: "10px",
      },
    },
    axisBorder: {
      show: true,
    },
    axisTicks: {
      show: true,
    },
  },
  yaxis: {
    show: true,
    color: "#fff",
    labels: {
      show: true,
      style: {
        colors: "#fff",
        fontSize: "10px",
        fontFamily: "Plus Jakarta Display",
      },
    },
  },
  grid: {
    show: true,
  },
  fill: {
    colors: "#fff",
  },
  dataLabels: {
    enabled: false,
  },
  plotOptions: {
    bar: {
      borderRadius: 8,
      columnWidth: "12px",
    },
  },
  responsive: [
    {
      breakpoint: 768,
      options: {
        plotOptions: {
          bar: {
            borderRadius: 0,
          },
        },
      },
    },
  ],
};
