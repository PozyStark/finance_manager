/* eslint-disable react/prop-types */
// @mui material components
import Icon from "@mui/material/Icon";

// Vision UI Dashboard React components
import VuiBox from "components/VuiBox";
import VuiTypography from "components/VuiTypography";
import VuiProgress from "components/VuiProgress";

// Images
import Jira from "examples/Icons/Jira";


function Completion({ value, color }) {
  return (
    <VuiBox display="flex" flexDirection="column" alignItems="flex-start">
      <VuiTypography variant="button" color="white" fontWeight="medium" mb="4px">
        {value}%&nbsp;
      </VuiTypography>
      <VuiBox width="8rem">
        <VuiProgress value={value} color={color} sx={{ background: "#2D2E5F" }} label={false} />
      </VuiBox>
    </VuiBox>
  );
}

const action = (
  <Icon sx={{ cursor: "pointer", fontWeight: "bold" }} fontSize="small">
    more_vert
  </Icon>
);

export default {
  columns: [
    { name: "Проект", align: "left" },
    { name: "Бюджет", align: "left" },
    { name: "Статус", align: "left" },
    { name: "Прогресс", align: "center" },
    { name: "Исправить", align: "center" },
  ],

  rows: [
    {
      Проект: (
        <VuiBox display="flex" alignItems="center">
          <Jira size="20px" />
          <VuiTypography pl="16px" color="white" variant="button" fontWeight="medium">
            Купить носки
          </VuiTypography>
        </VuiBox>
      ),
      Бюджет: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          10000
        </VuiTypography>
      ),
      Статус: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          Готово
        </VuiTypography>
      ),
      Прогресс: <Completion value={60} color="info" />,
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
          ...
        </VuiTypography>
      ),
      action,
    },
    {
      Проект: (
        <VuiBox display="flex" alignItems="center">
          <Jira size="20px" />
          <VuiTypography pl="16px" color="white" variant="button" fontWeight="medium">
          Купить носки
          </VuiTypography>
        </VuiBox>
      ),
      Бюджет: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
         10000
        </VuiTypography>
      ),
      Статус: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          Готово
        </VuiTypography>
      ),
      Прогресс: <Completion value={60} color="info" />,
      Исправить: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          ...
        </VuiTypography>
      ),
      action,
    },
    {
      Проект: (
        <VuiBox display="flex" alignItems="center">
          <Jira size="20px" />
          <VuiTypography pl="16px" color="white" variant="button" fontWeight="medium">
          Купить носки
          </VuiTypography>
        </VuiBox>
      ),
      Бюджет: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          10000
        </VuiTypography>
      ),
      Статус: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          Готово
        </VuiTypography>
      ),
      Прогресс: <Completion value={60} color="info" />,
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
          ...
        </VuiTypography>
      ),
      action,
    },
    {
      Проект: (
        <VuiBox display="flex" alignItems="center">
          <Jira size="20px" />
          <VuiTypography pl="16px" color="white" variant="button" fontWeight="medium">
          Купить носки
          </VuiTypography>
        </VuiBox>
      ),
      Бюджет: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          10000
        </VuiTypography>
      ),
      Статус: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          Готово
        </VuiTypography>
      ),
      Прогресс: <Completion value={60} color="info" />,
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
        ...
      </VuiTypography>
      ),
      action,
    },
    {
      Проект: (
        <VuiBox display="flex" alignItems="center">
          <Jira size="20px" />
          <VuiTypography pl="16px" color="white" variant="button" fontWeight="medium">
          Купить носки
          </VuiTypography>
        </VuiBox>
      ),
      Бюджет: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          10000
        </VuiTypography>
      ),
      Статус: (
        <VuiTypography variant="button" color="white" fontWeight="medium">
          Готово
        </VuiTypography>
      ),
      Прогресс: <Completion value={60} color="info" />,
      Исправить: (
        <VuiTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
        ...
      </VuiTypography>
      ),
      action,
    },
  ],
};
