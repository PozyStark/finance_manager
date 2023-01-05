/* eslint-disable react/prop-types */
// Vision UI Dashboard React components
import VuiBox from "components/VuiBox";
import VuiTypography from "components/VuiTypography";
import VuiAvatar from "components/VuiAvatar";

// Images

import magaz from "assets/images/5.png";



function Author({ image, name, info }) {
  return (
    <VuiBox display="flex" alignItems="center" px={1} py={0.5}>
      <VuiBox mr={2}>
        <VuiAvatar src={image} alt={name} size="sm" variant="rounded" />
      </VuiBox>
      <VuiBox display="flex" flexDirection="column">
        <VuiTypography variant="button" color="white" fontWeight="medium">
          {name}
        </VuiTypography>
        <VuiTypography variant="caption" color="text">
          {info}
        </VuiTypography>
      </VuiBox>
    </VuiBox>
  );
}

function Function({ job, org }) {
  return (
    <VuiBox display="flex" flexDirection="column">
      <VuiTypography variant="caption" fontWeight="medium" color="white">
        {job}
      </VuiTypography>
      <VuiTypography variant="caption" color="text">
        {org}
      </VuiTypography>
    </VuiBox>
  );
}

export default {
  columns: [
    { name: "Автор", align: "left" },
    { name: "Сумма", align: "center" },
    { name: "Дата", align: "center" },
    { name: "Исправить", align: "center" },
  ],

  rows: [
    {
      Автор: <Author image={magaz} name="Пятерочка" info="Кредитка" />,
      Сумма: (
        10000
      ),
      Дата: (
        <VuiTypography variant="caption" color="white" fontWeight="medium">
          23.04.22
        </VuiTypography>
      ),
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
          ...
        </VuiTypography>
      ),
    },
    {
      Автор: <Author image={magaz} name="Пятерочка" info="Кредитка" />,
      Сумма: (
        10000
      ),
      Дата: (
        <VuiTypography variant="caption" color="white" fontWeight="medium">
           23.04.22
        </VuiTypography>
      ),
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
          ...
        </VuiTypography>
      ),
    },
    {
      Автор: <Author image={magaz} name="Пятерочка" info="Наличные" />,
      Сумма: (
        10000
      ),
      Дата: (
        <VuiTypography variant="caption" color="white" fontWeight="medium">
           23.04.22
        </VuiTypography>
      ),
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
        ...
        </VuiTypography>
      ),
    },
    {
      Автор: <Author image={magaz} name="Пятерочка" info="Кредитка" />,
      Сумма: (
        10000
      ),
      Дата: (
        <VuiTypography variant="caption" color="white" fontWeight="medium">
           23.04.22
        </VuiTypography>
      ),
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
         ...
        </VuiTypography>
      ),
    },
    {
      Автор: <Author image={magaz} name="Пятерочка" info="Кредитка" />,
      Сумма: (
        10000
      ),
      Дата: (
        <VuiTypography variant="caption" color="white" fontWeight="medium">
           23.04.22
        </VuiTypography>
      ),
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
          ...
        </VuiTypography>
      ),
    },
    {
      Автор: <Author image={magaz} name="Пятерочка" info="Наличные"/>,
      Сумма: (
        10000
      ),
      Дата: (
        <VuiTypography variant="caption" color="white" fontWeight="medium">
           23.04.22
        </VuiTypography>
      ),
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
          ...
        </VuiTypography>
      ),
    },
  ],
};
