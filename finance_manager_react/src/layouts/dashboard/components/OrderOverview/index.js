// @mui material components
import Card from "@mui/material/Card";

// Vision UI Dashboard React components
import VuiBox from "components/VuiBox";
import VuiTypography from "components/VuiTypography";

// React icons
import { BsCheckCircleFill } from "react-icons/bs";
import { FaBell } from "react-icons/fa";
import { IoLogoCss3 } from "react-icons/io";
import { FaShoppingCart } from "react-icons/fa";
import { BsCreditCardFill } from "react-icons/bs";
import { SiDropbox } from "react-icons/si";

// Vision UI Dashboard React example components
import TimelineItem from "examples/Timeline/TimelineItem";
import AdobeXD from "examples/Icons/AdobeXD";

// Vision UI Dashboard theme imports
import palette from "assets/theme/base/colors";

function OrdersOverview() {
  return (
    <Card className="h-100">
      <VuiBox mb="16px">
        <VuiTypography variant="lg" fontWeight="bold" mb="5px" color="white">
          События
        </VuiTypography>
      </VuiBox>
      <VuiBox>
        <TimelineItem
          icon={<BsCreditCardFill size="16px" color={palette.warning.main} />}
          title="Оплачено картой 4545, 1200"
          dateTime="22 Декабря 22:10"
        />
        <TimelineItem
           icon={<BsCreditCardFill size="16px" color={palette.warning.main} />}
          title="Оплачено картой 4545, 1200"
          dateTime="22 Декабря 22:10"
        />
        <TimelineItem
          icon={<BsCreditCardFill size="16px" color={palette.warning.main} />}
          title="Оплачено картой 4545, 1200"
          dateTime="22 Декабря 22:10"
        />
        <TimelineItem
          icon={<BsCreditCardFill size="16px" color={palette.warning.main} />}
          title="Оплачено картой 4545, 1200"
          dateTime="22 Декабря 22:10"
        />
        <TimelineItem
          icon={<BsCreditCardFill size="16px" color={palette.warning.main} />}
          title="Оплачено картой 4545, 1200"
          dateTime="22 Декабря 22:10"
        />
      </VuiBox>
    </Card>
  );
}

export default OrdersOverview;
