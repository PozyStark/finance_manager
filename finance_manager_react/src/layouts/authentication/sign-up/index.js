import { useState } from "react";

// react-router-dom components
import { Link } from "react-router-dom";

// @mui material components
import Icon from "@mui/material/Icon";
import IconButton from "@mui/material/IconButton";
import Stack from "@mui/material/Stack";

// Icons
import { FaApple, FaFacebook, FaGoogle } from "react-icons/fa";

// Vision UI Dashboard React components
import VuiBox from "components/VuiBox";
import VuiTypography from "components/VuiTypography";
import VuiInput from "components/VuiInput";
import VuiButton from "components/VuiButton";
import VuiSwitch from "components/VuiSwitch";
import GradientBorder from "examples/GradientBorder";

// Vision UI Dashboard assets
import radialGradient from "assets/theme/functions/radialGradient";
import rgba from "assets/theme/functions/rgba";
import palette from "assets/theme/base/colors";
import borders from "assets/theme/base/borders";

// Authentication layout components
import CoverLayout from "layouts/authentication/components/CoverLayout";

// Images
import bgSignIn from "assets/images/signUpImage.png";

function SignIn() {
  const [rememberMe, setRememberMe] = useState(true);

  const handleSetRememberMe = () => setRememberMe(!rememberMe);

  return (
    <CoverLayout>
      <GradientBorder borderRadius={borders.borderRadius.form} minWidth="100%" maxWidth="100%" >
        <VuiBox
          component="form"
          role="form"
          borderRadius="inherit"
          p="45px"
          sx={({ palette: { secondary } }) => ({
            backgroundColor: secondary.focus,
          })}
        >
          <VuiTypography
            color="white"
            fontWeight="bold"
            textAlign="center"
            mb="12px"
            sx={({ typography: { size } }) => ({
              fontSize: size.lg,
            })}
          >
            Авторизация
          </VuiTypography>
          
          <VuiBox mb={2}>
            <VuiBox mb={1} ml={0.5}>
              <VuiTypography component="label" variant="button" color="white" fontWeight="medium">
                Email
              </VuiTypography>
            </VuiBox>
            <GradientBorder
              minWidth="100%"
              borderRadius={borders.borderRadius.lg}
              padding="1px"
              backgroundImage={radialGradient(
                palette.gradients.borderLight.main,
                palette.gradients.borderLight.state,
                palette.gradients.borderLight.angle
              )}
            >
              <VuiInput
                type="email"
                placeholder="Ваш email..."
                sx={({ typography: { size } }) => ({
                  fontSize: size.sm,
                })}
              />
            </GradientBorder>
          </VuiBox>
          <VuiBox mb={2}>
            <VuiBox mb={1} ml={0.5}>
              <VuiTypography component="label" variant="button" color="white" fontWeight="medium">
                Пароль
              </VuiTypography>
            </VuiBox>
            <GradientBorder
              minWidth="100%"
              borderRadius={borders.borderRadius.lg}
              padding="1px"
              backgroundImage={radialGradient(
                palette.gradients.borderLight.main,
                palette.gradients.borderLight.state,
                palette.gradients.borderLight.angle
              )}
            >
              <VuiInput
                type="password"
                placeholder="Ваш пароль..."
                sx={({ typography: { size } }) => ({
                  fontSize: size.sm,
                })}
              />
            </GradientBorder>
          </VuiBox>
          <VuiBox display="flex" alignItems="center">
            <VuiSwitch color="info" checked={rememberMe} onChange={handleSetRememberMe} />
            <VuiTypography
              variant="caption"
              color="white"
              fontWeight="medium"
              onClick={handleSetRememberMe}
              sx={{ cursor: "pointer", userSelect: "none" }}
            >
              &nbsp;&nbsp;&nbsp;&nbsp;Запомнить меня
            </VuiTypography>
          </VuiBox>
          <VuiBox mt={1} mb={1}>
            <VuiButton color="info" fullWidth
            component={Link}
            to="/dashboard">
              Авторизация
            </VuiButton>
          </VuiBox>
          <VuiBox mt={1} textAlign="center">
            <VuiTypography variant="button" color="text" fontWeight="regular">
              У вас нету аккаунта?{" "}
              <VuiTypography
                component={Link}
                to="/authentication/sign-in"
                variant="button"
                color="white"
                fontWeight="medium"
              >
                Регистрация
              </VuiTypography>
            </VuiTypography>
          </VuiBox>
        </VuiBox>
      </GradientBorder>
      </CoverLayout>
  );
}

export default SignIn;
