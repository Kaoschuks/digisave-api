private function phoneauth() 
    {
        include_once('../model/api.php');
        $app_id = '1941345565993784';
        $secret = 'e33b752a1f8a9acd8c49a41e4cc9d6bc';
        $version = 'v1.2';

        if (!isset($_POST['csrf']) || !isset($_POST['code']) || !isset($_POST['access'])) {
            BruteForce::initialize(false);
            return Response::json(400, "Missing paramaters in request");
        }

        $token_exchange_url = $version.'/access_token?grant_type=authorization_code&code='.$_POST['code']."&access_token=AA|$app_id|$secret";

        $data = api::getApiData($token_exchange_url);
        if (isset($data['error'])) {
            return Response::json(500, ($data) ? $data['error']['message'] : 'Connection to host no possible');
        }

        $user_id = $data['id'];
        $user_access_token = $data['access_token'];
        $refresh_interval = $data['token_refresh_interval_sec'];
        
        // Get Account Kit information
        $me_endpoint_url = $version.'/me?access_token='.$user_access_token;
        $data = api::getApiData($me_endpoint_url);
        if (isset($data['error'])) {
            return Response::json(500, $data['error']['message']);
        }

        return Response::json(
            200,
            array(
                "jwt" => Token::generateToken($_POST['access']),
                "data" => array(
                    "access" => $_POST['access'],
                    "uid" => $data['id'],
                    "mobile" => isset($data['phone']) ? $data['phone']['number'] : ''
                ),
            )
            
        );
    }