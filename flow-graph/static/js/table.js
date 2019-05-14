
$(document).ready(function()
{
    $('#data_table').DataTable(
    {
        "paging":   false,
        "searching": false,
        "info": false,
        "responsive": true
    })

    // Fill color for clean display
    $(".indic").each(function(i)
    {
        let value = $(this).data("value")

        // We want only red/green for non forced
        if(i%14 == 11)
        {
            if (value == 'True')
            {
                $(this).addClass("table-bg-5")
            }else
            {
                $(this).addClass("table-bg-1")
            }
        }
        // We want color for social ambiance good/none/bad
        else if (i%14 == 13)
        {
            switch(value.toLowerCase())
            {
                case 'bonne':
                    $(this).addClass("table-bg-5")
                    break
                case 'neutre':
                    $(this).addClass("table-bg-3")
                    break
                case 'négative':
                    $(this).addClass("table-bg-1")
                    break
            }
        }
        else
        {
            // Round if this is the first element of each row (flow indicator)
            if(i%14 == 0)
            {
               value = Math.round(parseFloat(value))
            } else if (i%14 == 12)
            {
                value = Math.round(parseFloat(value)/2)
            }
            $(this).addClass("table-bg-"+value)
        }
    })

    // Theoretical flow
    $(".theoretical_flow").each(function(i){
        let value = $(this).data("value")
        let canal = 0

        switch(value.toLowerCase())
        {
            case 'stimulé':
                canal = 1
                break
            case 'flow':
                canal = 2
                break
            case 'contrôle':
                canal = 3
                break
            case 'relaxation':
                canal = 4
                break
            case 'ennui':
                canal = 5
                break
            case 'apathie':
                canal = 6
                break
            case 'inquietude':
                canal = 7
                break
            case 'angoisse':
                canal = 8
                break
        }

        $(this).addClass("flow-"+canal)
    })
})