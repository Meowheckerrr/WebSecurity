class CustomError extends Error {
    constructor(message) {
      super(message);
      this.name = 'CustomError';
    }
  }
  
  // 使用自定义错误类型
  try {
    throw new CustomError('This is a custom error message.');
  } catch (error) {
    if (error instanceof CustomError) {
      console.error(`Caught a custom error: ${error.message}`);
    } else {
      console.error('Caught an error of unknown type.');
    }
  }