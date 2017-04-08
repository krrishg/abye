class Requests:
    def __init__(self):
        """initializes the data that is in json format
        """
        self.data = {
            'loan':
                {
                    'home_loan':
                        {
                            'sid bank':
                                {
                                    'interest': 7,
                                    'max_amount': 200000
                                },

                            'krrish bank':
                                {
                                    'interest': 50,
                                    'max_amount': 10000000
                                }
                        },

                    'student_loan':
                        {
                            'sid bank':
                                {
                                    'interest': 1,
                                    'max_amount': 1000000
                                },
                            'krrish bank':
                                {
                                    'interest': 10,
                                    'max_amount': 10000000
                                }
                        },
                    'car_loan':
                        {
                            'sid bank':
                                {
                                    'interest': 2,
                                    'max_amount': 4000000
                                },
                            'krrish bank':
                                {
                                    'interest': 1,
                                    'max_amount': 1000000
                                }
                        }

                },
            'deposit':
                {
                    'saving_account':
                        {
                            'sid bank':
                                {
                                    'interest': 6,
                                    'min_balance': 500
                                },
                            'krrish bank':
                                {
                                    'interest': 05,
                                    'min_balance': 30
                                }
                        },
                    'fixed_account':
                        {
                            'sid bank':
                                {
                                    'interest': 7,
                                    'min_balance': 10000
                                },
                            'krrish bank':
                                {
                                    'interest': 5,
                                    'min_balance': 30000
                                }
                        },
                    'special_account':
                        {
                            'sid bank':
                                {
                                    'interest': 8,
                                    'min_balance': 1000000,
                                    'debit_amount': 10000000
                                },
                            'krrish bank':
                                {
                                    'interest': 10,
                                    'min_balance': 300000,
                                    'debit_amount': 10000000
                                }
                        }
                }
        }

    def get_loan(self, type=None):
        """
        It handles get request for loans
        
        :param type:[optional] type of loan::
           if type is specified:
              :returns: dictionary of type of loan
           else
              :returns: dictionary of all loans
        """
        loan = self.data['loan']
        data = {}
        if type:  # if type is specified
            if type in loan.keys():  # check whether the type is available or not
                data = {
                    'status': 'valid',
                    'loan_type': type,
                }
                data.update(loan[type])
            else:
                data = {
                    'status': 'invalid',
                    'message': 'loan type not found'
                }
        else:  # if type is not specified
            data = {
                'status': 'valid'
            }
            data.update(loan)
        return data

    def get_deposit(self, type=None):
        """
        It handles get request for deposit

        :param type:[optional] type of deposit ::
           if type is specified:
              :returns: dictionary of type of deposit
           else
              :returns: dictionary of all deposits
        """
        deposit = self.data['deposit']
        data = {}
        if type:  # if type is specified
            if type in deposit.keys():  # check whether type is available or not
                data = {
                    'status': 'valid',
                    'deposit_type': type
                }
                data.update(deposit[type])
            else:
                data = {
                    'status': 'invalid',
                    'message': 'deposit type not found'
                }
        else:  # if type is not specified
            data = {
                'status': 'valid'
            }
            data.update(deposit)
        return data
