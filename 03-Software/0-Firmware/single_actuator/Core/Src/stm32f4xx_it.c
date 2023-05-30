/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file    stm32f4xx_it.c
  * @brief   Interrupt Service Routines.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32f4xx_it.h"
/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN TD */

/* USER CODE END TD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define INNER_GEAR_RATIO 40
#define MIDDLE_GEAR_RATIO 40*5
#define OUTER_GEAR_RATIO 40
#define DUTY_PERCENTAGE_LIMIT 0.95

#define	BUF_SIZE	8
#define ANTI_WIND_UP 40
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
/* USER CODE BEGIN PV */

/* USB related */
extern int16_t move_x;
extern int16_t move_y;

char command_byte;

char error_code = 0;
uint8_t external_shutdown = 0;
uint8_t ack_to_be_sent = 0;
uint8_t steady_state_counter = 0;



uint16_t i;
uint16_t led_bool;
uint8_t usb_out[BUF_SIZE] = "Hello world from USB. \n";
uint8_t blink_led_cmd[BUF_SIZE];
uint8_t usb_in[BUF_SIZE];
uint8_t check_receive;
uint8_t usb_temp[BUF_SIZE];

uint8_t empty_string[BUF_SIZE] = "";
uint8_t acknowledge_message[BUF_SIZE] = "a\n";
uint8_t error_message[BUF_SIZE] = "e\n";

/* Define and initialize the encoder and motor position variables (pulse counters) */
int enc_inner_pos = 0;
int enc_middle_pos = 0;
int enc_outer_pos = 0;

float enc_inner_pos_cm = 0;
float enc_middle_pos_cm = 0;
float enc_outer_pos_cm = 0;

/* Position set */
float mot_inner_set_pos = 0;
float mot_middle_set_pos = 0;
float mot_outer_set_pos = 0;

extern float X_curr;
extern float X_ref;


/* PID related*/
extern uint32_t PID_freq;

float inner_pos_error=0.0;
float middle_pos_error=0.0;
float outer_pos_error=0.0;
float pre_inner_pos_error=0.0;
float pre_middle_pos_error=0.0;
float pre_outer_pos_error=0.0;
float inner_int_error=0.0;
float middle_int_error=0.0;
float outer_int_error=0.0;

float kp_inner=1500.0;
float ki_inner=1500.0;
float kd_inner=0.0;

float kp_middle=1500.0;
float ki_middle=1500.0;
float kd_middle=0.0;

float kp_outer=1500.0;
float ki_outer=1500.0;
float kd_outer=0.0;


/* PWM-Specific Variables */
int duty_inner = 0;
int duty_middle = 0;
int duty_outer = 0;

/* Define pin state */
GPIO_PinState LOW = 0;
GPIO_PinState HIGH = 1;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
/* USER CODE BEGIN PFP */
extern uint8_t CDC_Transmit_FS(uint8_t* Buf, uint16_t Len);
extern int8_t CDC_Receive_FS(uint8_t* Buf, uint32_t Len);

extern void inverse_kinematics();
extern void forward_kinematics();
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/* External variables --------------------------------------------------------*/
extern PCD_HandleTypeDef hpcd_USB_OTG_FS;
extern TIM_HandleTypeDef htim3;
extern TIM_HandleTypeDef htim4;
/* USER CODE BEGIN EV */
extern TIM_HandleTypeDef htim1;
/* USER CODE END EV */

/******************************************************************************/
/*           Cortex-M4 Processor Interruption and Exception Handlers          */
/******************************************************************************/
/**
  * @brief This function handles Non maskable interrupt.
  */
void NMI_Handler(void)
{
  /* USER CODE BEGIN NonMaskableInt_IRQn 0 */

  /* USER CODE END NonMaskableInt_IRQn 0 */
  /* USER CODE BEGIN NonMaskableInt_IRQn 1 */
  while (1)
  {
  }
  /* USER CODE END NonMaskableInt_IRQn 1 */
}

/**
  * @brief This function handles Hard fault interrupt.
  */
void HardFault_Handler(void)
{
  /* USER CODE BEGIN HardFault_IRQn 0 */

  /* USER CODE END HardFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_HardFault_IRQn 0 */
    /* USER CODE END W1_HardFault_IRQn 0 */
  }
}

/**
  * @brief This function handles Memory management fault.
  */
void MemManage_Handler(void)
{
  /* USER CODE BEGIN MemoryManagement_IRQn 0 */

  /* USER CODE END MemoryManagement_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_MemoryManagement_IRQn 0 */
    /* USER CODE END W1_MemoryManagement_IRQn 0 */
  }
}

/**
  * @brief This function handles Pre-fetch fault, memory access fault.
  */
void BusFault_Handler(void)
{
  /* USER CODE BEGIN BusFault_IRQn 0 */

  /* USER CODE END BusFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_BusFault_IRQn 0 */
    /* USER CODE END W1_BusFault_IRQn 0 */
  }
}

/**
  * @brief This function handles Undefined instruction or illegal state.
  */
void UsageFault_Handler(void)
{
  /* USER CODE BEGIN UsageFault_IRQn 0 */

  /* USER CODE END UsageFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_UsageFault_IRQn 0 */
    /* USER CODE END W1_UsageFault_IRQn 0 */
  }
}

/**
  * @brief This function handles System service call via SWI instruction.
  */
void SVC_Handler(void)
{
  /* USER CODE BEGIN SVCall_IRQn 0 */

  /* USER CODE END SVCall_IRQn 0 */
  /* USER CODE BEGIN SVCall_IRQn 1 */

  /* USER CODE END SVCall_IRQn 1 */
}

/**
  * @brief This function handles Debug monitor.
  */
void DebugMon_Handler(void)
{
  /* USER CODE BEGIN DebugMonitor_IRQn 0 */

  /* USER CODE END DebugMonitor_IRQn 0 */
  /* USER CODE BEGIN DebugMonitor_IRQn 1 */

  /* USER CODE END DebugMonitor_IRQn 1 */
}

/**
  * @brief This function handles Pendable request for system service.
  */
void PendSV_Handler(void)
{
  /* USER CODE BEGIN PendSV_IRQn 0 */

  /* USER CODE END PendSV_IRQn 0 */
  /* USER CODE BEGIN PendSV_IRQn 1 */

  /* USER CODE END PendSV_IRQn 1 */
}

/**
  * @brief This function handles System tick timer.
  */
void SysTick_Handler(void)
{
  /* USER CODE BEGIN SysTick_IRQn 0 */

  /* USER CODE END SysTick_IRQn 0 */
  HAL_IncTick();
  /* USER CODE BEGIN SysTick_IRQn 1 */

  /* USER CODE END SysTick_IRQn 1 */
}

/******************************************************************************/
/* STM32F4xx Peripheral Interrupt Handlers                                    */
/* Add here the Interrupt Handlers for the used peripherals.                  */
/* For the available peripheral interrupt handler names,                      */
/* please refer to the startup file (startup_stm32f4xx.s).                    */
/******************************************************************************/

/**
  * @brief This function handles EXTI line0 interrupt.
  */
void EXTI0_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI0_IRQn 0 */
	/* Check the direction of the first motor */
	if(HAL_GPIO_ReadPin(GPIOA, ENC1_B_Pin)){
		/* Update the position of the first motor */
		enc_inner_pos ++;
	}else{
		enc_inner_pos --;
	}
	enc_inner_pos_cm = (float)enc_inner_pos/(float)(INNER_GEAR_RATIO);
  /* USER CODE END EXTI0_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC1_A_Pin);
  /* USER CODE BEGIN EXTI0_IRQn 1 */

  /* USER CODE END EXTI0_IRQn 1 */
}

/**
  * @brief This function handles EXTI line2 interrupt.
  */
void EXTI2_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI2_IRQn 0 */
	/* Check the direction of the second motor */
		if(HAL_GPIO_ReadPin(GPIOA, ENC2_B_Pin)){
			/* Update the position of the first motor */
			enc_middle_pos ++;
		}else{
			enc_middle_pos --;
		}
		enc_middle_pos_cm = (float)enc_middle_pos/(float)(MIDDLE_GEAR_RATIO);
  /* USER CODE END EXTI2_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC2_A_Pin);
  /* USER CODE BEGIN EXTI2_IRQn 1 */

  /* USER CODE END EXTI2_IRQn 1 */
}

/**
  * @brief This function handles EXTI line4 interrupt.
  */
void EXTI4_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI4_IRQn 0 */
	/* Check the direction of the third motor */
		if(HAL_GPIO_ReadPin(GPIOA, ENC3_B_Pin)){
			/* Update the position of the first motor */
			enc_outer_pos ++;
		}else{
			enc_outer_pos --;
		}
		enc_outer_pos_cm = (float)enc_outer_pos/(float)(OUTER_GEAR_RATIO);
  /* USER CODE END EXTI4_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC3_A_Pin);
  /* USER CODE BEGIN EXTI4_IRQn 1 */

  /* USER CODE END EXTI4_IRQn 1 */
}

/**
  * @brief This function handles TIM3 global interrupt.
  */
void TIM3_IRQHandler(void)
{
  /* USER CODE BEGIN TIM3_IRQn 0 */

  /* USER CODE END TIM3_IRQn 0 */
  HAL_TIM_IRQHandler(&htim3);
  /* USER CODE BEGIN TIM3_IRQn 1 */

  /* USER CODE END TIM3_IRQn 1 */
}

/**
  * @brief This function handles TIM4 global interrupt.
  */
void TIM4_IRQHandler(void)
{
  /* USER CODE BEGIN TIM4_IRQn 0 */

	if(error_code == 0 && external_shutdown == 0){

	/* Determine PID errors */
	inner_pos_error = mot_inner_set_pos - enc_inner_pos_cm;
	middle_pos_error = mot_middle_set_pos - enc_middle_pos_cm;
	outer_pos_error = mot_outer_set_pos - enc_outer_pos_cm;

	float inner_der_error=(inner_pos_error-pre_inner_pos_error)*PID_freq;
	float middle_der_error=(middle_pos_error-pre_middle_pos_error)*PID_freq;
	float outer_der_error=(outer_pos_error-pre_outer_pos_error)*PID_freq;

	inner_int_error+=inner_pos_error/PID_freq;
	middle_int_error+=middle_pos_error/PID_freq;
	outer_int_error+=outer_pos_error/PID_freq;

	if (inner_int_error>=ANTI_WIND_UP) inner_int_error=ANTI_WIND_UP;
	if (middle_int_error>=ANTI_WIND_UP) middle_int_error=ANTI_WIND_UP;
	if (outer_int_error>=ANTI_WIND_UP) outer_int_error=ANTI_WIND_UP;

	if (inner_int_error<=-ANTI_WIND_UP) inner_int_error=-ANTI_WIND_UP;
	if (middle_int_error<=-ANTI_WIND_UP) middle_int_error=-ANTI_WIND_UP;
	if (outer_int_error<=-ANTI_WIND_UP) outer_int_error=-ANTI_WIND_UP;

	if (((inner_pos_error>0) && (inner_int_error<0))||((inner_pos_error<0) && (inner_int_error>0))) inner_int_error=0;
	if (((middle_pos_error>0) && (middle_int_error<0))||((middle_pos_error<0) && (middle_int_error>0))) middle_int_error=0;
	if (((outer_pos_error>0) && (outer_int_error<0))||((outer_pos_error<0) && (outer_int_error>0))) outer_int_error=0;

	pre_inner_pos_error=inner_pos_error;
	pre_middle_pos_error=middle_pos_error;
	pre_outer_pos_error=outer_pos_error;

	/* Set the duty (only proportional implemented for now) */
	duty_inner = (int)((kp_inner*inner_pos_error)+(kd_inner*inner_der_error)+(ki_inner*inner_int_error));
	duty_middle = (int)(kp_middle*middle_pos_error+kd_middle*middle_der_error+ki_middle*middle_int_error);
	duty_outer = (int)(kp_outer*outer_pos_error+kd_outer*outer_der_error+ki_outer*outer_int_error);

	/* Set the direction (MOTOR CONNECTIONS REVERSED!!!) */
	if(duty_inner > 0){
			HAL_GPIO_WritePin(GPIOB, IN1_A_Pin, LOW);
			HAL_GPIO_WritePin(GPIOB, IN1_B_Pin, HIGH);
	}
	else{
			duty_inner = -duty_inner;
			HAL_GPIO_WritePin(GPIOB, IN1_B_Pin, LOW);
			HAL_GPIO_WritePin(GPIOB, IN1_A_Pin, HIGH);
	}
	if(duty_middle > 0){
			HAL_GPIO_WritePin(GPIOB, IN2_A_Pin, LOW);
			HAL_GPIO_WritePin(GPIOB, IN2_B_Pin, HIGH);
	}
	else{
			duty_middle = -duty_middle;
			HAL_GPIO_WritePin(GPIOB, IN2_B_Pin, LOW);
			HAL_GPIO_WritePin(GPIOB, IN2_A_Pin, HIGH);
	}
	if(duty_outer > 0){
			HAL_GPIO_WritePin(GPIOB, IN3_A_Pin, LOW);
			HAL_GPIO_WritePin(GPIOB, IN3_B_Pin, HIGH);
	}
	else{
			duty_outer = -duty_outer;
			HAL_GPIO_WritePin(GPIOB, IN3_B_Pin, LOW);
			HAL_GPIO_WritePin(GPIOB, IN3_A_Pin, HIGH);
	}

	/* Limit the duty */
	if(duty_inner > ((htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT)){
			duty_inner = (htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT;
		}
	if(duty_middle > ((htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT)){
			duty_middle = (htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT;
		}
	if(duty_outer > ((htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT)){
			duty_outer = (htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT;
		}
	TIM1->CCR1 = duty_inner;
	TIM1->CCR2 = duty_middle;
	TIM1->CCR3 = duty_outer;

	// Send acknowledge if the system reaches steady state
	if (ack_to_be_sent == 1 && fabs(inner_pos_error) <= 0.5 && fabs(middle_pos_error) <= 0.5 && fabs(outer_pos_error) <= 0.5){
		steady_state_counter++;
		if (steady_state_counter == 255){
			forward_kinematics();
			memcpy(&usb_out, &acknowledge_message, sizeof(usb_out));
			CDC_Transmit_FS(usb_out, sizeof(usb_out));
			ack_to_be_sent = 0;
		}
	}
	else {
		steady_state_counter = 0;
	}

	}
	else{
		TIM1->CCR1 = 0;
		TIM1->CCR2 = 0;
		TIM1->CCR3 = 0;
		memcpy(&usb_out, &error_message, sizeof(usb_out));
		CDC_Transmit_FS(usb_out, sizeof(usb_out));
	}
  /* USER CODE END TIM4_IRQn 0 */
  HAL_TIM_IRQHandler(&htim4);
  /* USER CODE BEGIN TIM4_IRQn 1 */

  /* USER CODE END TIM4_IRQn 1 */
}

/**
  * @brief This function handles USB On The Go FS global interrupt.
  */
void OTG_FS_IRQHandler(void)
{
  /* USER CODE BEGIN OTG_FS_IRQn 0 */

	CDC_Receive_FS(usb_temp,sizeof(usb_temp));

	if(strcmp((char *)usb_temp, (char *)empty_string) != 0){
		HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);

		// Store the data in usb_in array if a non-empty message received
		memcpy(&usb_in, &usb_temp, sizeof(usb_in));

		/* Parsing USB Message*/
		if(usb_in[0] == 'm'){
			move_x = usb_in[1]*256 + usb_in[2];
			move_y = usb_in[3]*256 + usb_in[4];

			/* FOR DEBUGGING PURPOSES
			usb_in[1] = move_x/256;
			usb_in[2] = move_x%256;
			usb_in[3] = move_y/256;
			usb_in[4] = move_y%256;
			usb_in[5] = '\n';
			CDC_Transmit_FS(usb_in,sizeof(usb_in));
			*/

			X_ref = X_curr + (float)move_x/10;

			// Apply inverse kinematics to update set values
			inverse_kinematics();
			ack_to_be_sent = 1;

		}
		if(usb_in[0] == 's'){
			external_shutdown = 1;
		}
		if(usb_in[0] == 'i'){
			// NOT USED FOR NOW
		}
		if(usb_in[0] == 'o'){
			// TURN OFF CODE TO BE ADDED
		}
		if(usb_in[0] == 'b'){
			// BEGIN COMMAND
		}

	}

	// Clear usb_temp array
	memset(usb_temp, 0, sizeof(usb_temp));

  /* USER CODE END OTG_FS_IRQn 0 */
  HAL_PCD_IRQHandler(&hpcd_USB_OTG_FS);
  /* USER CODE BEGIN OTG_FS_IRQn 1 */

  /* USER CODE END OTG_FS_IRQn 1 */
}

/* USER CODE BEGIN 1 */

/* USER CODE END 1 */
