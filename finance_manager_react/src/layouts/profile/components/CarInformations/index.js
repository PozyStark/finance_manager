
import React from 'react';
import { Card, Stack, Grid } from '@mui/material';
import VuiBox from 'components/VuiBox';
import VuiTypography from 'components/VuiTypography';
import GreenLightning from 'assets/images/shapes/green-lightning.svg';
import WhiteLightning from 'assets/images/shapes/white-lightning.svg';
import linearGradient from 'assets/theme/functions/linearGradient';
import colors from 'assets/theme/base/colors';
import carProfile from 'assets/images/shapes/car-profile.svg';
import LineChart from 'examples/Charts/LineCharts/LineChart';
import { lineChartDataProfile1, lineChartDataProfile2 } from 'variables/charts';
import { lineChartOptionsProfile2, lineChartOptionsProfile1 } from 'variables/charts';
import CircularProgress from '@mui/material/CircularProgress';
const CarInformations = () => {
	const { gradients, info } = colors;
	const { cardContent } = gradients;
	return (
		<Card
			sx={({ breakpoints }) => ({
				[breakpoints.up('xxl')]: {
					maxHeight: '400px'
				}
			})}>
			<VuiBox display='flex' flexDirection='column'>
				<VuiTypography variant='lg' color='white' fontWeight='bold' mb='6px'>
					Баланс счета
				</VuiTypography>
			
				<Stack
					spacing='24px'
					background='#fff'
					sx={({ breakpoints }) => ({
						[breakpoints.up('sm')]: {
							flexDirection: 'column'
						},
						[breakpoints.up('md')]: {
							flexDirection: 'row'
						},
						[breakpoints.only('xl')]: {
							flexDirection: 'column'
						}
					})}>
					<VuiBox
						display='flex'
						flexDirection='column'
						justifyContent='center'
						sx={({ breakpoints }) => ({
							[breakpoints.only('sm')]: {
								alignItems: 'center'
							}
						})}
						alignItems='center'>
						
					</VuiBox>
					<Grid
						container
						sx={({ breakpoints }) => ({
							spacing: '24px',
							[breakpoints.only('sm')]: {
								columnGap: '0px',
								rowGap: '24px'
							},
							[breakpoints.up('md')]: {
								gap: '24px',
								ml: '50px !important'
							},
							[breakpoints.only('xl')]: {
								gap: '12px',
								mx: 'auto !important'
							}
						})}>
						<Grid item xs={12} md={5.5} xl={5.8} xxl={5.5}>
							<VuiBox
								display='flex'
								p='18px'
								alignItems='center'
								sx={{
									background: linearGradient(cardContent.main, cardContent.state, cardContent.deg),
									minHeight: '110px',
									borderRadius: '20px'
								}}>
								<VuiBox display='flex' flexDirection='column' mr='auto'>
									<VuiTypography color='text' variant='caption' fontWeight='medium' mb='2px'>
										Баланс
									</VuiTypography>
									<VuiTypography
										color='white'
										variant='h4'
										fontWeight='bold'
										sx={({ breakpoints }) => ({
											[breakpoints.only('xl')]: {
												fontSize: '20px'
											}
										})}>
										1111
									</VuiTypography>
								</VuiBox>
								<VuiBox
									display='flex'
									justifyContent='center'
									alignItems='center'
									sx={{
										background: info.main,
										borderRadius: '12px',
										width: '56px',
										height: '56px'
									}}>
									<VuiBox />
								</VuiBox>
							</VuiBox>
						</Grid>
						<Grid item xs={12} md={5.5} xl={5.8} xxl={5.5}>
							<VuiBox
								display='flex'
								p='18px'
								alignItems='center'
								sx={{
									background: linearGradient(cardContent.main, cardContent.state, cardContent.deg),
									minHeight: '110px',
									borderRadius: '20px'
								}}>
								<VuiBox display='flex' flexDirection='column' mr='auto'>
									<VuiTypography color='text' variant='caption' fontWeight='medium' mb='2px'>
										Долг
									</VuiTypography>
									<VuiTypography
										color='white'
										variant='h4'
										fontWeight='bold'
										sx={({ breakpoints }) => ({
											[breakpoints.only('xl')]: {
												fontSize: '20px'
											}
										})}>
										1111
									</VuiTypography>
								</VuiBox>
								<VuiBox
									display='flex'
									justifyContent='center'
									alignItems='center'
									sx={{
										background: info.main,
										borderRadius: '12px',
										width: '56px',
										height: '56px'
									}}>
									<VuiBox />
								</VuiBox>
							</VuiBox>
						</Grid>
					</Grid>
				</Stack>
			</VuiBox>
		</Card>
	);
};

export default CarInformations;
